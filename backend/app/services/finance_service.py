from backend.app.models.finance import Finance
from backend.app.schemas import FinanceUpdate
from backend.app.core.database import SessionLocal

def get_finance_summary(user_id: int):
    db = SessionLocal()
    finance = db.query(Finance).filter(Finance.user_id == user_id).first()
    db.close()
    return finance

def update_finance(user_id: int, finance_data: FinanceUpdate):
    db = SessionLocal()
    finance = db.query(Finance).filter(Finance.user_id == user_id).first()
    if finance:
        finance.total_income += finance_data.income
        finance.total_expenses += finance_data.expenses
        db.commit()
        db.refresh(finance)
    db.close()
    return finance