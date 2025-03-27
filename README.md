Loan Management System (LMS)

A FastAPI-based Loan Management System that integrates with a CORE Banking System (CBS) and a Scoring Engine. This system allows users to subscribe, request loans, and check loan status while handling customer KYC and transaction data via SOAP APIs.

🚀 Features

User Authentication: Secure login via OAuth2/JWT

Customer Subscription: Register customers for loan services

Loan Requests & Status Checks: API endpoints for loan processing

CORE Banking Integration: Fetch customer KYC and transaction history via SOAP APIs

Scoring Engine Integration: Credit scoring and loan limit calculations

Async Processing with Celery: Handle retries for failed Scoring Engine requests

Logging & Monitoring: Track API usage and errors

Modular & Scalable Architecture

🛠️ Tech Stack

FastAPI - API framework

SQLite - Lightweight database

SQLAlchemy - ORM for database interactions

Celery - Async task queue

OAuth2 + JWT - Secure authentication

SOAP & REST APIs - External integrations

📂 Project Structure

bash
Copy
Edit
loan_management_system/
│── app/
│   ├── routers/        # API route handlers
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic models
│   ├── crud/           # Database operations
│   ├── utils/          # Helper functions
│   ├── config.py       # Application settings
│── database.py         # Database connection
│── main.py             # Application entry point
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── .env                # Environment variables



🔧 Setup & Installation

1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/BenDev254/loan-management-system.git
cd loan-management-system

2️⃣ Create a Virtual Environment
sh
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt

4️⃣ Set Up Environment Variables
Create a .env file and add:

env
Copy
Edit
DATABASE_URL=sqlite:///./loan_db.sqlite
SECRET_KEY=your-secret-key

5️⃣ Run Database Migrations
sh
Copy
Edit
python database.py

6️⃣ Start the Application
sh
Copy
Edit
uvicorn main:app --reload

7️⃣ Access the API Docs
Swagger UI: http://127.0.0.1:8000/docs

Redoc UI: http://127.0.0.1:8000/redoc

📌 API Endpoints
🔹 Authentication
Method	Endpoint	Description
POST	/auth/login	Login and get a JWT token

🔹 Customer Management
Method	Endpoint	Description
POST	/subscribe	Subscribe a customer

🔹 Loan Processing
Method	Endpoint	Description
POST	/loan/request	Request a loan
GET	/loan/status	Check loan status

🏗️ Future Improvements
Docker deployment

PostgreSQL migration

Azure DevOps pipeline integration

More advanced logging and monitoring

🛠 Contributing

Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Added a new feature")

Push to the branch (git push origin feature-branch)

Open a Pull Request
