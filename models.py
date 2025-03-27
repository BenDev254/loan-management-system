from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    customer_number = Column(String, ForeignKey("kyc.customer_number"), index=True)
    amount = Column(Float)
    status = Column(String, default="Pending")

    customer = relationship("KYC", back_populates="loans")


class KYC(Base):
    __tablename__ = "kyc"
    id = Column(Integer, primary_key=True, index=True)
    customer_number = Column(String, unique=True, index=True)
    name = Column(String)
    dob = Column(String)

    loans = relationship("Loan", back_populates="customer")
    transactions = relationship("Transaction", back_populates="customer")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    customer_number = Column(String, ForeignKey("kyc.customer_number"), index=True)
    transaction_details = Column(String)

    customer = relationship("KYC", back_populates="transactions")


class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    customer_number = Column(String, ForeignKey("kyc.customer_number"), unique=True, nullable=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    service_type = Column(String, nullable=True)
    status = Column(String, default="active")
    created_at = Column(DateTime, server_default=func.now())

    customer = relationship("KYC")
