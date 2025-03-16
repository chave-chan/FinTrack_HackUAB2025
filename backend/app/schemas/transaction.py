from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: int
    user_id: int
    amount: float
    type: str  # "income" or "expense"
    category: str
    date: datetime

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    type: str
    category: str