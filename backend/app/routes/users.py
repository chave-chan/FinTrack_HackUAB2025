from fastapi import APIRouter, HTTPException
from backend.app.models.user import User
from backend.app.core.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def list_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users