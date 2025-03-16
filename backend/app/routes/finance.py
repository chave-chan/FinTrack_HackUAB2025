from fastapi import APIRouter, HTTPException
from backend.app.services.finance_service import get_finance_summary, update_finance
from backend.app.schemas import FinanceUpdate

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.get("/{user_id}")
async def finance_summary(user_id: int):
    summary = get_finance_summary(user_id)
    if not summary:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return summary

@router.put("/{user_id}")
async def update_finances(user_id: int, finance: FinanceUpdate):
    return update_finance(user_id, finance)