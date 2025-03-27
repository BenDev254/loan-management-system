import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./lms.db")

# CORE Banking System (CBS) SOAP Credentials
CBS_USERNAME = os.getenv("CBS_USERNAME", "admin")
CBS_PASSWORD = os.getenv("CBS_PASSWORD", "pwd123")

# Scoring Engine API
SCORING_BASE_URL = "https://scoringtest.credable.io/api/v1/scoring"
CLIENT_REGISTRATION_URL = "https://scoringtest.credable.io/api/v1/client/createClient"

# WSDL Links
KYC_WSDL = "https://kycapitest.credable.io/service/customerWsdl.wsdl"
TRANSACTIONS_WSDL = "https://trxapitest.credable.io/service/transactionWsdl.wsdl"

# Retry Mechanism
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
