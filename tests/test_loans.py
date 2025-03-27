import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app  # Import your FastAPI app
from models import Loan

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the dependency to use test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create tables before running tests
Base.metadata.create_all(bind=engine)

# Initialize test client
client = TestClient(app)

# Provided test customer IDs
TEST_CUSTOMERS = [234774784, 318411216, 340397370, 366585630, 397178638]

@pytest.fixture(scope="function")
def setup_test_db():
    """Clear database before each test"""
    db = TestingSessionLocal()
    db.query(Loan).delete()
    db.commit()
    db.close()

@pytest.mark.usefixtures("setup_test_db")
@pytest.mark.parametrize("customer_id", TEST_CUSTOMERS)
def test_apply_for_loan_success(customer_id):
    """Test loan application success"""
    response = client.post(
        "/loans/",  # Adjust if needed
        json={"customer_id": customer_id, "amount": 1000}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == str(customer_id)
    assert data["amount"] == 1000
    assert data["status"] == "Pending"

@pytest.mark.usefixtures("setup_test_db")
@pytest.mark.parametrize("customer_id", TEST_CUSTOMERS)
def test_apply_for_loan_duplicate(customer_id):
    """Test that a customer cannot apply for a new loan while having a pending loan"""
    client.post(
        "/loans/",
        json={"customer_id": customer_id, "amount": 1000}
    )
    response = client.post(
        "/loans/",
        json={"customer_id": customer_id, "amount": 2000}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Active loan request exists"

@pytest.mark.usefixtures("setup_test_db")
@pytest.mark.parametrize("customer_id", TEST_CUSTOMERS)
def test_apply_for_loan_invalid_amount(customer_id):
    """Test loan application with invalid amount"""
    response = client.post(
        "/loans/",
        json={"customer_id": customer_id, "amount": -500}
    )
    assert response.status_code == 422  # FastAPI handles validation

@pytest.mark.usefixtures("setup_test_db")
@pytest.mark.parametrize("customer_id", TEST_CUSTOMERS)
def test_apply_for_loan_missing_data(customer_id):
    """Test loan application with missing fields"""
    response = client.post(
        "/loans/",
        json={"amount": 1000}  # Missing customer_id
    )
    assert response.status_code == 422  # FastAPI validation error
