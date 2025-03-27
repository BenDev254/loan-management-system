import requests
from config import settings
from schemas.cbs import KYCRequest, KYCResponse, TransactionRequest, TransactionResponse

KYC_SOAP_URL = "https://kycapitest.credable.io/service/customerWsdl.wsdl"
TRANSACTION_SOAP_URL = "https://trxapitest.credable.io/service/transactionWsdl.wsdl"

def get_kyc_data(request: KYCRequest) -> KYCResponse:
    # Simulate SOAP request (replace with actual SOAP implementation)
    response = requests.get(f"{KYC_SOAP_URL}?customer_number={request.customer_number}")

    if response.status_code == 200:
        data = response.json()
        return KYCResponse(
            customer_number=data["customer_number"],
            name=data["name"],
            dob=data["dob"]
        )
    else:
        return None

def get_transaction_data(request: TransactionRequest) -> TransactionResponse:
    # Simulate SOAP request
    response = requests.get(f"{TRANSACTION_SOAP_URL}?customer_number={request.customer_number}")

    if response.status_code == 200:
        data = response.json()
        return TransactionResponse(
            customer_number=data["customer_number"],
            transaction_details=data["transaction_details"]
        )
    else:
        return None