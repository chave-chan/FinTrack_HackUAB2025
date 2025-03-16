from fastapi import APIRouter, HTTPException
from backend.app.services.education_service import get_educational_content, create_educational_content
from backend.app.schemas import EducationalContentCreate

router = APIRouter(prefix="/education", tags=["Education"])

@router.get("/")
async def list_content():
    return get_educational_content()

@router.post("/")
async def add_content(content: EducationalContentCreate):
    return create_educational_content(content)