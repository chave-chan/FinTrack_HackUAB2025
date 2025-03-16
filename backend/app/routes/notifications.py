from fastapi import APIRouter
from backend.app.services.notifications_service import get_notifications

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.get("/{user_id}")
async def list_notifications(user_id: int):
    return get_notifications(user_id)