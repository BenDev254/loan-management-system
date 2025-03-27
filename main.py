from fastapi import FastAPI
from app.routers import auth, loans, cbs, scoring
from database import engine, Base

app = FastAPI(title="Loan Management System")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])
app.include_router(cbs.router, prefix="/cbs", tags=["Core Banking System"])
app.include_router(scoring.router, prefix="/scoring", tags=["Scoring Engine"])

@app.get("/")
def root():
    return {"message": "Loan Management System API"}
