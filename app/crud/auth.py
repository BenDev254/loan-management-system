from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from schemas.auth import AuthRequest, Token
from models import User
from sqlalchemy.orm import Session
from config import settings


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def login(db: Session, request: AuthRequest) -> Token:
    user = authenticate_user(db, request.username, request.password)
    if not user:
        return None

    access_token = create_access_token({"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")
