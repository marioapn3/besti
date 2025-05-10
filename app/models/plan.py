from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FeatureQuotas(BaseModel):
    documents_per_month: int
    integrations: int
    team_members: int

class AddOn(BaseModel):
    name: str
    description: str
    price: float

class Plan(BaseModel):
    _id: str
    name: str
    description: str
    pricing_model: str
    price: float
    feature_quotas: FeatureQuotas
    trial_enabled: bool
    trial_duration_days: int
    billing_cycle: str
    add_ons: Optional[List[AddOn]] = []
    is_active: bool
    created_at: str
    updated_at:  str
