from zeep import Client
from config import KYC_WSDL_URL, TRANSACTION_WSDL_URL, SOAP_USERNAME, SOAP_PASSWORD

def get_customer_kyc(customer_number: str):
    client = Client(KYC_WSDL_URL)
    return client.service.GetCustomerKYC(customer_number, SOAP_USERNAME, SOAP_PASSWORD)

def get_customer_transactions(customer_number: str):
    client = Client(TRANSACTION_WSDL_URL)
    return client.service.GetCustomerTransactions(customer_number, SOAP_USERNAME, SOAP_PASSWORD)


TRANSACTION_WSDL = "https://trxapitest.credable.io/service/transactionWsdl.wsdl"

def fetch_transaction_data(customer_number: str):
    """
    Queries the SOAP Transactions API to retrieve customer transactions.
    """
    client = Client(TRANSACTION_WSDL)
    response = client.service.getCustomerTransactions(customerNumber=customer_number)
    return response
