from fastapi import APIRouter, HTTPException
from backend.app.services.transaction_service import get_transactions, create_transaction
from backend.app.schemas import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/{user_id}")
async def list_transactions(user_id: int):
    return get_transactions(user_id)

@router.post("/")
async def add_transaction(transaction: TransactionCreate):
    return create_transaction(transaction)