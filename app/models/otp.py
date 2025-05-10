from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from bson import ObjectId 


class OTP(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    email: EmailStr
    otp: str
    is_used: bool
    expires_at: str  # ISO format
    created_at: str  # ISO format

    class Config:
        # This allows Pydantic to work with MongoDB ObjectId as a string
        json_encoders = {
            ObjectId: str
        }
