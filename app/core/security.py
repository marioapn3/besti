from passlib.context import CryptContext
from typing import Union, Any
from app.core.config import settings
from datetime import datetime, timedelta
import jwt
import random
from loguru import logger
from itsdangerous import URLSafeTimedSerializer


# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_hash_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

# Generate OTP
def generate_otp() -> str:
    otp = str(random.randint(100000, 999999)) 
    return otp

# JWT Token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_DAYS * 24 * 60)) -> bytes:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM_SECRET_KEY)
    logger.info(f"JWT Token: {encoded_jwt}")

    return encoded_jwt

def decode_token(token):
    data = jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=settings.JWT_ALGORITHM_SECRET_KEY,
    )

    return data

serializer = URLSafeTimedSerializer(
    secret_key=settings.JWT_SECRET_KEY, salt="email-configuration"
)

def create_url_safe_token(data: dict):

    token = serializer.dumps(data)

    return token

def decode_url_safe_token(token:str):
    try:
        token_data = serializer.loads(token)
        
        return token_data
    
    except Exception as e:
        logger.error(str(e))
        