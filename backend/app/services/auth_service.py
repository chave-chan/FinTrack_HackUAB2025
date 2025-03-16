from backend.app.models.user import User
from backend.app.schemas import UserCreate
from backend.app.core.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(user: UserCreate):
    db = SessionLocal()
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, full_name=user.full_name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
