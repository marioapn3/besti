from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class MessageRequest(BaseModel):
    session_id : str = Field(..., title="Session ID")
    query : str = Field(..., title="Show revenue trend from invoice data")