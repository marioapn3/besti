from datetime import datetime, timedelta

from bson import ObjectId
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

from app.core.config import settings
from app.db.database import messages_collection
from app.services.session_service import SessionService
from typing import List
import requests
import json

from app.core.config import settings
class MessageService:
    @staticmethod
    def create_message(session_id: str, role: str, content: str) -> str:
        now = datetime.now().isoformat()

        message_data = {
            "session_id": session_id,
            "role": role,
            "content": content,
            "created_at": now,
            "updated_at": now,
        }

        count = messages_collection.count_documents({"session_id": session_id})
        if count == 0:
            SessionService.update_session(session_id, {"title": content})

        result = messages_collection.insert_one(message_data)

        return str(result.inserted_id)
    
    @staticmethod
    async def m_create_message(session_id: str, role: str, content: str) -> str:
        now = datetime.now().isoformat()

        message_data = {
            "session_id": session_id,
            "role": role,
            "content": content,
            "created_at": now,
            "updated_at": now,
        }

        # Menggunakan count_documents dengan await
        count = await messages_collection.count_documents({"session_id": session_id})
        
        if count == 0:
            await SessionService.m_update_session(session_id, {"title": content})

        # Menggunakan insert_one dengan await
        result = await messages_collection.insert_one(message_data)

        return str(result.inserted_id)

    @staticmethod
    def get_message_count(session_id: str):
        return messages_collection.count_documents({"session_id": session_id})

    @staticmethod
    def get_messages(session_id: str):
        messages = messages_collection.find({
            "session_id": session_id,
        }).sort("created_at", ASCENDING)

        return messages
    
    @staticmethod
    def get_message_history(session_id: str) -> List[dict]:
        messages = list(messages_collection.find({"session_id": session_id}))
        # Convert ObjectId to string for JSON serialization
        for message in messages:
            if "_id" in message:
                message["_id"] = str(message["_id"])
        return messages

    @staticmethod
    def load_messages_history(session_id: str):
        chat_history = []
        for message in messages_collection.find({"session_id": session_id}).sort("created_at", ASCENDING):
            chat_history.append({
                "role": message["role"],
                "content": message["content"],
            })
        
        if not chat_history:
            chat_history.append({
                "role": "system",
                "content": "Hello! How can I help you today?",
            })
        return chat_history

    @staticmethod
    def get_messages_history(session_id: str):
        chat_history = []
        for message in messages_collection.find({"session_id": session_id}).sort("created_at", ASCENDING):
            chat_history.append({
                "role": message["role"],
                "content": message["content"],
                "created_at": message["created_at"]
            })
        return chat_history

    @staticmethod
    def get_title(session_id: str):
        message = messages_collection.find_one({"session_id": session_id})
        return message["content"] if message else "Untitled"

    @staticmethod
    def get_first_message(session_id: str):
        message = messages_collection.find_one({"session_id": session_id})
        return message["content"] if message else "Untitled"

    