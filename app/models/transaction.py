from pydantic import BaseModel
from typing import List

class TransactionItem(BaseModel):
    name: str
    price: float
    quantity: int

class TransactionCreate(BaseModel):
    customer_id: str
    organisation_id: Optional[str]
    amount: float
    currency: str
    items: List[TransactionItem]
