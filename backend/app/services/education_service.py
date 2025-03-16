from backend.app.models.education import Education
from backend.app.schemas import EducationalContentCreate
from backend.app.core.database import SessionLocal

def get_educational_content():
    db = SessionLocal()
    content = db.query(Education).all()
    db.close()
    return content

def create_educational_content(content_data: EducationalContentCreate):
    db = SessionLocal()
    new_content = Education(**content_data.dict())
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    db.close()
    return new_content
