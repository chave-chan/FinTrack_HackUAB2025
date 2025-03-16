from pydantic import BaseModel

class EducationalContent(BaseModel):
    id: int
    title: str
    description: str
    category: str

    class Config:
        from_attributes = True

class EducationalContentCreate(BaseModel):
    title: str
    description: str
    category: str