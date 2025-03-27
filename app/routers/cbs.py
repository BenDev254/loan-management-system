import zeep
from fastapi import APIRouter, HTTPException
from config import KYC_WSDL, TRANSACTIONS_WSDL, CBS_USERNAME, CBS_PASSWORD

router = APIRouter()

@router.get("/kyc/{customer_number}")
def get_customer_kyc(customer_number: str):
    client = zeep.Client(wsdl=KYC_WSDL)
    response = client.service.GetCustomerInfo(CBS_USERNAME, CBS_PASSWORD, customer_number)
    return response

@router.get("/transactions/{customer_number}")
def get_customer_transactions(customer_number: str):
    client = zeep.Client(wsdl=TRANSACTIONS_WSDL)
    response = client.service.GetTransactions(CBS_USERNAME, CBS_PASSWORD, customer_number)
    return response
