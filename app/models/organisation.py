# { "name": "Tech Corp", "industry": "Information Technology", "address": "123 Main St, City, Country", "type": "SMB" }

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class Organisations(BaseModel):
    id: str = Field(..., alias="_id")  
    customer_id: str
    name: str
    industry: str
    slug: str
    address: str  
    city: str
    country: str
    created_at: str 
    updated_at: str 



