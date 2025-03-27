
import requests
from zeep import Client
from config import settings
from schemas.transactions import TransactionResponse
from typing import List

def get_customer_transactions(customer_id: str) -> List[TransactionResponse]:
    """Fetch customer transactions from the SOAP API."""
    
    try:
        # Initialize SOAP client
        client = Client(settings.SOAP_TRANSACTION_URL)

        # Call the SOAP service
        response = client.service.GetTransactions(customerId=customer_id)

        # Transform the response into a list of TransactionResponse objects
        transactions = [
            TransactionResponse(
                transaction_id=txn["transactionId"],
                customer_id=txn["customerId"],
                amount=txn["amount"],
                date=txn["date"],
                status=txn["status"]
            )
            for txn in response["transactions"]
        ]

        return transactions

    except Exception as e:
        print(f"Error fetching transactions: {e}")
        return []