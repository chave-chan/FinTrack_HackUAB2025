import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "FinTrack"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/fintrack")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    PERPLEXITY_API_KEY: str = os.getenv("PERPLEXITY_API_KEY", "")
    PAY_RETAILERS_API_KEY: str = os.getenv("PAY_RETAILERS_API_KEY", "")

settings = Settings()
