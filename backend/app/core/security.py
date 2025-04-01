from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
from app.core.config import settings

def create_access_token(
    user_id: str,
    expires_delta: Optional[timedelta] = None
) -> str:
    """Создает JWT токен для аутентификации"""
    to_encode = {"sub": str(user_id)}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )