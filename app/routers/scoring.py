import requests
from fastapi import APIRouter, HTTPException
from config import SCORING_BASE_URL
from soap_client import fetch_transaction_data

router = APIRouter()

@router.get("/score/{customer_number}")
def get_credit_score(customer_number: str):
    # Step 1: Initiate Query Score
    response = requests.get(f"{SCORING_BASE_URL}/initiateQueryScore/{customer_number}")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to initiate scoring")

    token = response.json().get("token")

    # Step 2: Query Score (Retry Mechanism)
    for _ in range(3):  
        score_response = requests.get(f"{SCORING_BASE_URL}/queryScore/{token}")
        if score_response.status_code == 200:
            return score_response.json()
    raise HTTPException(status_code=500, detail="Scoring Engine did not respond in time")



@router.get("/transactions/{customer_number}")
def expose_transactions(customer_number: str):
    """
    Allows the Scoring Engine to fetch transactions for a customer.
    """
    transactions = fetch_transaction_data(customer_number)
    return transactions


@router.get("/initiate/{customer_number}")
def initiate_score_query(customer_number: str):
    """
    Initiates a credit score query for a customer.
    """
    response = requests.get(f"https://scoringtest.credable.io/api/v1/scoring/initiateQueryScore/{customer_number}")
    return response.json()


@router.post("/register")
def register_lms():
    """
    Registers LMS with the Scoring Engine.
    """
    payload = {
        "url": "http://localhost:3000/api/v1/transactions",
        "name": "LoanManagementSystem",
        "username": "admin",
        "password": "pwd123"
    }
    response = requests.post("https://scoringtest.credable.io/api/v1/client/createClient", json=payload)
    return response.json()



@router.get("/query/{token}")
def query_score(token: str):
    """
    Retrieves a customer's credit score using the token.
    """
    response = requests.get(f"https://scoringtest.credable.io/api/v1/scoring/queryScore/{token}")
    return response.json()
