from sqlalchemy.orm import Session
from models import User  # Import the User model

def get_user(db: Session, username: str):
    """Retrieve a user by their username."""
    return db.query(User).filter(User.username == username).first()
