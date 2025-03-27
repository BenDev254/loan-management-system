import requests
from config import settings

def get_kyc_data(customer_id: str):
    """Fetch customer KYC details from CORE Banking System (SOAP API)."""
    url = f"{settings.CORE_BANKING_URL}/kyc"
    payload = {"customerId": customer_id}
    response = requests.post(url, json=payload)
    return response.json()

def initiate_score(customer_id: str):
    """Initiate score request to Scoring Engine."""
    url = f"{settings.SCORING_ENGINE_URL}/score/initiate"
    payload = {"customerId": customer_id}
    response = requests.post(url, json=payload)
    return response.json()

def fetch_score(token: str):
    """Retrieve credit score using token."""
    url = f"{settings.SCORING_ENGINE_URL}/score/retrieve"
    payload = {"token": token}
    response = requests.post(url, json=payload)
    return response.json()
