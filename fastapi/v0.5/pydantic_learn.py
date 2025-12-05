# pydantic in fastapi is used to declare the shape of requests and response
from typing import Any
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    age: int
    gender: str
    email: str
    is_active: bool
    last_login: datetime | None
    friends: list[int] | None


u1: dict[str, Any] = {
    "id": 0,
    "username": "abc",
    "age": 20,
    "gender": "M",
    "email": "abc@example.com",
    "is_active": "false",
    "last_login": "2017-06-01 12:22",
    "friends": None,
}

U1: User = User(**u1)  # unpacking dictionary as arguments
print(U1)
