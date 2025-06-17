import os
from io import BytesIO
import requests
from pathlib import Path
import imghdr
import base64
import json
import time
import asyncio
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from fastapi import BackgroundTasks, APIRouter, Depends, HTTPException, Request, Form, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from typing import List, Optional
from uuid import uuid4
import imghdr
import base64
import json
import time
import asyncio

from loguru import logger
from fpdf import FPDF, Align
    
# LangChain Imports
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.document_loaders import PyPDFLoader

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_vertexai import ChatVertexAI

# Add these imports after the existing langchain imports
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter

# Application Schemas


from app.schemas.message import MessageRequest

# Middleware
from app.middleware.jwt import JWTBearer

# Configurations
from app.core.config import settings

# Services
from app.services.message_service import MessageService
from app.services.session_service import SessionService

# Services Langchain
from app.services.langchains.embeddings import get_google_embedding
from app.services.langchains.vector_stores import get_chroma_vector_store
from app.services.langchains.api_keys import APIKeyManager
from app.services.langchains.llms import load_llm

# Utilities
from app.utils.helper import clean_extracted_response
from app.utils.messages.error import ERR_MSG
from app.utils.messages.success import SUCCESS_MESSAGES
from app.utils.response import generate_response, generate_response_error, generate_paginated_response
# from app.utils.prompt.helper import MESSAGE_SYSTEM_PROMPT

# from langchain.cache import RedisSemanticCache
from langchain_community.vectorstores.redis import Redis as RedisVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Setup embeddings dan RedisSemanticCache
APIKeyManager.setup_api_keys()
chroma_vectors = get_chroma_vector_store()
os.environ['USER_AGENT'] = 'myagent'
router = APIRouter()

@router.get('/session/{session_id}', response_model=dict)
def get_session_by_id(session_id: str):
    try: 
        session = SessionService.get_session_by_id(session_id)
        message_history = MessageService.get_message_history(session_id)
        
        if not session:
            raise ValueError("session_not_found")
        return generate_response({
            "session": session,
            "message_history": message_history
        }, SUCCESS_MESSAGES["retrieved_session"], True, 200)
    except ValueError as e:
        logger.error("Error : " + str(e))
        err = ERR_MSG.get(str(e), ERR_MSG["internal_server_error"])
        return generate_response_error(err, err["response_code"])
    except Exception as e:
        logger.error(f"Error: {e}")
        return generate_response_error(ERR_MSG["internal_server_error"], 500)

@router.post("/session", response_model=dict)
def create_session():
    try:
        session = SessionService.create_session()
        return generate_response(  session,SUCCESS_MESSAGES["session_created"])
    except Exception as e:
        logger.error(f"Error: {e}")
        return generate_response_error(ERR_MSG["internal_server_error"], 500) 

@router.post("/message", response_model=dict)
def create_message(request: Request, data: MessageRequest):
    try:
        session_id = data.session_id
        message = data.query
        session = SessionService.get_session_by_id(session_id)
        
        # Retrieve relevant documents from ChromaDB
        retriever = chroma_vectors.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}  # Get top 3 most relevant documents
        )
        relevant_docs = retriever.get_relevant_documents(data.query)
        
        # Combine relevant documents into context
        context = "\n".join([doc.page_content for doc in relevant_docs])
        logger.info(context)
        
        system_message = f"""
            Anda adalah chatbot akademik Universitas Dian Nuswantoro yang melayani mahasiswa.
            Berikut adalah informasi yang relevan untuk menjawab pertanyaan:

            {context}

            Jawablah pertanyaan mahasiswa di bawah dengan padat dan jelas berdasarkan informasi di atas.
            Jika informasi di atas tidak cukup untuk menjawab pertanyaan, berikan jawaban umum yang informatif.
        """

        # Format messages untuk Gemini API
        messages = []
        messages.append({"role": "model", "parts": [{"text": system_message}]})
        
        # Tambahkan message history
        message_history = MessageService.get_message_history(session_id)
        for msg in message_history:
            if msg["role"] == "human":
                messages.append({"role": "user", "parts": [{"text": msg["content"]}]})
            else:
                messages.append({"role": "model", "parts": [{"text": msg["content"]}]})

        # Tambahkan pertanyaan terakhir
        messages.append({"role": "user", "parts": [{"text": data.query}]})

        logger.info(messages)

        # Siapkan request ke Gemini API dengan retry logic
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={settings.GEMINI_API_KEY}"
        headers = {
            'Content-Type': 'application/json'
        }
        payload = {
            "contents": messages
        }

        # Configure retry strategy
        retry_strategy = Retry(
            total=3,  # number of retries
            backoff_factor=1,  # wait 1, 2, 4 seconds between retries
            status_forcelist=[500, 502, 503, 504],  # HTTP status codes to retry on
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)

        # Kirim request ke Gemini API dengan timeout
        try:
            response = session.post(url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()  # Raise an exception for bad status codes
            response_data = response.json()
            model_response = response_data['candidates'][0]['content']['parts'][0]['text']
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            return generate_response_error({"message": "Failed to connect to AI service. Please try again later."}, 503)

        # Save messages to history
        MessageService.create_message(session_id, "human", data.query)
        MessageService.create_message(session_id, "ai", model_response)

        return generate_response(model_response, SUCCESS_MESSAGES["generate_rag"], True, 201)
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        return generate_response_error(ERR_MSG["internal_server_error"], 500)

@router.post("/load-markdown", response_model=dict)
def load_markdown_files():
    try:
        # Path to the data directory
        data_dir = Path("public/data/Standardized Corpus")
        
        # Find all markdown files recursively
        markdown_files = list(data_dir.rglob("*.md"))
        
        if not markdown_files:
            return generate_response_error({"message": "No markdown files found"}, 404)
        
        # Load and process documents
        documents = []
        for file_path in markdown_files:
            try:
                loader = UnstructuredMarkdownLoader(str(file_path))
                documents.extend(loader.load())
            except Exception as e:
                logger.error(f"Error loading file {file_path}: {str(e)}")
                continue
        
        if not documents:
            return generate_response_error({"message": "No documents could be loaded"}, 400)
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        splits = text_splitter.split_documents(documents)
        
        # Add documents to ChromaDB
        chroma_vectors.add_documents(splits)
        
        return generate_response({
            "message": f"Successfully loaded {len(splits)} document chunks from {len(markdown_files)} files",
            "files_processed": len(markdown_files),
            "chunks_created": len(splits)
        }, "Documents loaded successfully", True, 200)
        
    except Exception as e:
        logger.error(f"Error loading markdown files: {str(e)}")
        return generate_response_error(ERR_MSG["internal_server_error"], 500)

@router.post("/load-markdown-v2", response_model=dict)
def load_markdown_files():
    try:
        # Path ke direktori data
        data_dir = Path("public/data/Standardized Corpus")
        
        # Ambil semua file markdown secara rekursif
        markdown_files = list(data_dir.rglob("*.md"))
        
        if not markdown_files:
            return generate_response_error({"message": "No markdown files found"}, 404)

        all_documents = []
        
        # Konfigurasi header markdown untuk chunking
        header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "heading_1"),
                ("##", "heading_2"),
                ("###", "heading_3"),
                ("####", "heading_4"),
            ]
        )
        
        for file_path in markdown_files:
            try:
                # Baca markdown sebagai string (bukan pakai loader dulu)
                with open(file_path, "r", encoding="utf-8") as f:
                    markdown_string = f.read()
                
                # Split berdasarkan struktur heading markdown
                md_chunks = header_splitter.split_text(markdown_string)

                # Ubah ke format Document untuk ChromaDB
                documents = [
                    Document(
                        page_content=chunk["content"],
                        metadata={
                            "source": str(file_path),
                            **chunk["metadata"]
                        }
                    )
                    for chunk in md_chunks
                ]

                all_documents.extend(documents)

            except Exception as e:
                logger.error(f"Error loading file {file_path}: {str(e)}")
                continue
        
        if not all_documents:
            return generate_response_error({"message": "No documents could be loaded"}, 400)

        # Tambahkan semua dokumen ke ChromaDB
        chroma_vectors.add_documents(all_documents)
        
        return generate_response({
            "message": f"Successfully loaded {len(all_documents)} document chunks from {len(markdown_files)} files",
            "files_processed": len(markdown_files),
            "chunks_created": len(all_documents)
        }, "Documents loaded successfully", True, 200)
    
    except Exception as e:
        logger.error(f"Error loading markdown files: {str(e)}")
        return generate_response_error(ERR_MSG["internal_server_error"], 500)
