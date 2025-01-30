from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRATION_TIME

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt