from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from app.core.config import settings

_embeddings = None

def get_google_embedding():
    global _embeddings
    if _embeddings is None:
        _embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=settings.GEMINI_API_KEY,
            task_type="retrieval_document"
        )
    return _embeddings


