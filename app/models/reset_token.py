from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from bson import ObjectId 

class ResetToken(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    email: EmailStr
    reset_token: str
    is_used: bool
    expires_at: str  # ISO format
    created_at: str  # ISO format

    class Config:
         json_encoders = {
            ObjectId: str
        }
