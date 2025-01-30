from fastapi import APIRouter
from models import UserCreate, User
from database import users_collection
from auth import create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    # Check if the username or email already exists in the database
    existing_user = users_collection.find_one({"$or": [{"username": user.username}, {"email": user.email}]})
    if existing_user:
        return {"error": "Username or email already exists"}

    # Create a new user in the database with a specified role and return it
    user_doc = user.dict()
    user_doc["role"] = "user"  # Set the default role to "user"
    result = users_collection.insert_one(user_doc)
    user.id = result.inserted_id
    return {"message": "User successfully registered", "user": user}

@router.post("/login")
def login(username: str, password: str):
    # Check the user credentials and return a token if valid
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        # Create a token (e.g., using JWT) and return it
        token = create_access_token(data={"sub": str(user.id)})
        return {"token": token}
    return {"error": "Invalid username or password"}