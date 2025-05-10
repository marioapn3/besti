from datetime import datetime, timedelta

from bson import ObjectId
from pymongo import ASCENDING
from pymongo.errors import DuplicateKeyError

from typing import Tuple
from app.core.config import settings
from app.db.database import sessions_collection, messages_collection

class SessionService:
    @staticmethod
    def create_session() -> str:    
        now = datetime.now().isoformat()

        session_data = {
            "created_at": now,
            "updated_at": now,
        }
        result = sessions_collection.insert_one(session_data)
        session = sessions_collection.find_one({"_id": result.inserted_id})
        session["_id"] = str(session["_id"])

        return session

    @staticmethod
    def get_session_by_id(session_id: str):
        session =  sessions_collection.find_one({"_id": ObjectId(session_id)})
        
        if session:
            session["_id"] = str(session["_id"])
        return session

    @staticmethod
    def update_session(session_id: str, data: dict):
        now = datetime.now().isoformat()
        data["updated_at"] = now
        sessions_collection.update_one({"_id": ObjectId(session_id)}, {"$set": data})

        session = sessions_collection.find_one({"_id": ObjectId(session_id)})
        session["_id"] = str(session["_id"])

        return session
    
    @staticmethod
    async def m_update_session(session_id: str, data: dict):
        now = datetime.now().isoformat()
        data["updated_at"] = now
        
        # Update the session
        await sessions_collection.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": data}
        )

        # Get the updated session
        session = await sessions_collection.find_one({"_id": ObjectId(session_id)})
        if session:
            session["_id"] = str(session["_id"])

        return session
    
    @staticmethod
    def update_session_token(session_id: str, token_used: int):
        now = datetime.now().isoformat()
        session = sessions_collection.find_one({"_id": ObjectId(session_id)})

        new_token_used = session["token_used"] + token_used

        sessions_collection.update_one({"_id": ObjectId(session_id)}, {"$set": {"token_used": new_token_used, "updated_at": now}})

        session = sessions_collection.find_one({"_id": ObjectId(session_id)})

        session["_id"] = str(session["_id"])

        return session


    @staticmethod
    def get_all_sessions( organisation_id: str):
        sessions_cursor = sessions_collection.find({"organisation_id": organisation_id})
        sessions = list(sessions_cursor)  
    
        for session in sessions:
            message = messages_collection.find_one({"session_id": str(session["_id"])})
            if session["title"] == "Untitled":
                if message and "content" in message:
                    sessions_collection.update_one({"_id": ObjectId(session["_id"])}, {"$set": {"title": message["content"]}})
            session["_id"] = str(session["_id"])
        
        return sessions
    
    @staticmethod
    def get_paginated_sessions(organisation_id: str, page: int, limit: int):
        sessions_cursor = (
        sessions_collection.find({"organisation_id": organisation_id})
        .sort("created_at", -1)  # Urutkan berdasarkan created_at descending
        .skip((page - 1) * limit)
        .limit(limit)
        )
        sessions = list(sessions_cursor)  

        for session in sessions:
            message = messages_collection.find_one({"session_id": str(session["_id"])})
            if session["title"] == "Untitled":
                if message and "content" in message:
                    sessions_collection.update_one({"_id": ObjectId(session["_id"])}, {"$set": {"title": message["content"]}})
            session["_id"] = str(session["_id"])

        return sessions, sessions_collection.count_documents({"organisation_id": organisation_id})

    
    @staticmethod
    def delete_session(session_id: str):
        session = sessions_collection.find_one({"_id": ObjectId(session_id)})
        messages_collection.delete_many({"session_id": str(session["_id"])})
        sessions_collection.delete_one({"_id": ObjectId(session_id)})
        return session


    # async all functions
    @staticmethod
    async def m_find_one(session_id: str):
        session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})
        if session is not None:
            session["_id"] = str(session["_id"])
            return session
        return None

    @staticmethod
    async def m_create_session(organisation_id: str, team_data: dict) -> dict:
        now = datetime.now().isoformat()
        session_data = {
            "organisation_id": organisation_id,
            "title": "Untitled",
            "created_at": now,
            "updated_at": now,
            "token_used": 0,
            "created_by": team_data
        }

        result = await m_sessions_collection.insert_one(session_data)
        session = await m_sessions_collection.find_one({"_id": result.inserted_id})
        session["_id"] = str(session["_id"])
        return session

    @staticmethod
    async def m_get_session_by_id(session_id: str) -> dict | None:
        session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})
        if session:
            session["_id"] = str(session["_id"])
        return session

    @staticmethod
    async def m_update_session(session_id: str, data: dict) -> dict | None:
        now = datetime.now().isoformat()
        data["updated_at"] = now

        await m_sessions_collection.update_one({"_id": ObjectId(session_id)}, {"$set": data})
        session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})
        if session:
            session["_id"] = str(session["_id"])
        return session

    @staticmethod
    async def m_update_session_token(session_id: str, token_used: int) -> dict | None:
        now = datetime.now().isoformat()
        session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})

        if not session:
            return None

        new_token_used = session["token_used"] + token_used
        await m_sessions_collection.update_one(
            {"_id": ObjectId(session_id)},
            {"$set": {"token_used": new_token_used, "updated_at": now}}
        )

        updated_session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})
        if updated_session:
            updated_session["_id"] = str(updated_session["_id"])
        return updated_session

    @staticmethod
    async def m_get_all_sessions(organisation_id: str) -> list:
        sessions_cursor = m_sessions_collection.find({"organisation_id": organisation_id})
        sessions = []
        async for session in sessions_cursor:
            session["_id"] = str(session["_id"])
            sessions.append(session)
        return sessions

    @staticmethod
    async def m_get_paginated_sessions(organisation_id: str, page: int, limit: int) -> Tuple[list, int]:
        skip = (page - 1) * limit
        sessions_cursor = m_sessions_collection.find({"organisation_id": organisation_id}).sort("created_at", -1).skip(skip).limit(limit)

        sessions = []
        async for session in sessions_cursor:
            session["_id"] = str(session["_id"])
            sessions.append(session)

        total = await m_sessions_collection.count_documents({"organisation_id": organisation_id})
        return sessions, total

    @staticmethod
    async def m_delete_session(session_id: str) -> dict | None:
        session = await m_sessions_collection.find_one({"_id": ObjectId(session_id)})
        if session:
            await m_sessions_collection.delete_one({"_id": ObjectId(session_id)})
            return {**session, "_id": str(session["_id"])}
        return None
