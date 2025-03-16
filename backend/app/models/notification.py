from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from backend.app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    read = Column(Boolean, default=False)