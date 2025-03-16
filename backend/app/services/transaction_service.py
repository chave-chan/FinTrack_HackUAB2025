from backend.app.models.transaction import Transaction
from backend.app.schemas import TransactionCreate
from backend.app.core.database import SessionLocal
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select

Base = declarative_base()

async def get_transactions(user_id: int):
    async with SessionLocal() as db:
        result = await db.execute(select(Transaction).where(Transaction.user_id == user_id))
        return result.scalars().all()


def create_transaction(transaction_data: TransactionCreate):
    db = SessionLocal()
    new_transaction = Transaction(**transaction_data.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    db.close()
    return new_transaction