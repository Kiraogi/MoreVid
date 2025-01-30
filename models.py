from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str

class User(UserCreate):
    id: int

class Video(BaseModel):
    title: str
    description: str
    url: str