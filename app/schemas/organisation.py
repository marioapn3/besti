from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

# Create a schema for the organisation
class OrganisationRequest(BaseModel):
    name: str = Field(..., example="Tech Corp")
    industry: str = Field(..., example="Information Technology")
    # address: str = Field(..., example="123 Main St, City, Country")
    # city: str = Field(..., example="City")
    # country: str = Field(..., example="Country")

# Update Request schema for updating an organisation
class OrganisationUpdateRequest(BaseModel):
    name: Optional[str] = Field(None, example="Tech Corp")
    industry: Optional[str] = Field(None, example="Information Technology")
    # address: Optional[str] = Field(None, example="123 Main St, City, Country")
    # city: Optional[str] = Field(None, example="City")
    # country: Optional[str] = Field(None, example="Country")
