from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Customer(BaseModel):
    id: str = Field(..., alias="_id")  # MongoDB uses "_id" as the primary key
    name: str
    email: EmailStr  # Validate email format
    subscription_plan: str  # e.g., "Founders", "SMB", "Enterprise"
    password: str
    is_verified: bool 
    role: str # admin, staff, viewer
    created_at: str # Timestamp in ISO format
    updated_at: str # Timestamp in ISO format
    # nullable
    industry_type: Optional[str] = None  # Nullable string
    organisation_ids: Optional[List[str]] = None  # Nullable list of strings



