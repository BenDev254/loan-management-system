from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from models import User
from security import create_access_token
from sqlalchemy.orm import Session
from schemas.auth import Token
from schemas.users import UserResponse
from jose import JWTError, jwt
from config import settings
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends

router = APIRouter()



@router.post("/login", response_model=Token)
def login(user: User):
    # Dummy check for now, can be replaced with DB lookup
    if user.username != "admin" or user.password != "pwd123":
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
async def read_users_me(
    db: Session = Depends(get_db),  # Assuming get_db is a dependency to get the database session
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)  # oauth2_scheme is your token retrieval scheme
):
    token_str = token.credentials  

    try:
        # Decode the JWT token
        payload = jwt.decode(token_str, settings.SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("sub")

        if not username:
            raise HTTPException(status_code=401, detail="Not authenticated")

        user = get_user(db, username)  # Call the function to get the user from the DB
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return UserResponse(
            id=user.id,
            username=user.username,
            full_name=user.full_name or "N/A",
            email=user.email or "N/A",
            is_active=user.is_active
        )

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
