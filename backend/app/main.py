from fastapi import FastAPI
from backend.app.routes import (
    auth_router,
    education_router,
    finance_router,
    notifications_router,
    transactions_router,
    users_router
)

app = FastAPI(title="FinTrack API", version="1.0")

app.include_router(auth_router)
app.include_router(education_router)
app.include_router(finance_router)
app.include_router(notifications_router)
app.include_router(transactions_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Bienvenido a FinTrack API"}