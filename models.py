from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

from pydantic import BaseModel


class Video(BaseModel):
    title: str
    description: str
    url: str