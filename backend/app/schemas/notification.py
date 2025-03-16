from pydantic import BaseModel

class NotificationBase(BaseModel):
    message: str
    user_id: int

class NotificationCreate(NotificationBase):
    pass

class NotificationRead(NotificationBase):
    id: int
    read: bool

    class Config:
        orm_mode = True