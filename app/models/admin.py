from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Admin(BaseModel):
    id: str = Field(..., alias="_id")  # MongoDB uses "_id" as the primary key
    name: str
    email: EmailStr  # Validate email format
    role: str  # e.g., superadmin, admin, support
    permissions : List[str] | None = None  #list of permissions
    is_active: bool 
    created_at: str
    updated_at: str



