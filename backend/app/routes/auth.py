from fastapi import APIRouter, HTTPException, Depends
from backend.app.schemas import UserCreate
from backend.app.models.user import User
from backend.app.services.auth_service import create_user, verify_password
from backend.app.core.database import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: UserCreate):
    db_user = create_user(user)
    if not db_user:
        raise HTTPException(status_code=400, detail="Error al crear usuario")
    return {"message": "Usuario registrado exitosamente"}

@router.post("/login")
async def login(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    db.close()
    
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"message": "Inicio de sesión exitoso"}