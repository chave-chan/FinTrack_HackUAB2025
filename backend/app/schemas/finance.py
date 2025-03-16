from pydantic import BaseModel

class FinanceSummary(BaseModel):
    user_id: int
    total_income: float
    total_expenses: float
    balance: float

class FinanceUpdate(BaseModel):
    income: float
    expenses: float