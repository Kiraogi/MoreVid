import jwt
from fastapi import APIRouter
from models import User
from database import users_collection

router = APIRouter()
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


def generate_token(user):
    # Создайте токен авторизации (например, с помощью JWT)
    payload = {"username": user["username"]}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

@router.post("/register")
def register(user: User):
    # Выполните проверку уникальности имени пользователя и сохраните данные пользователя в базе данных
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        return {"error": "Пользователь уже существует"}
    users_collection.insert_one(user.dict())
    return {"message": "Пользователь успешно зарегистрирован"}

@router.post("/login")
def login(username: str, password: str):
    # Выполните проверку учетных данных пользователя и верните токен авторизации
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        # Создайте токен авторизации (например, с помощью JWT) и верните его
        token = generate_token(user)
        return {"token": token}
    return {"error": "Неверный логин или пароль"}