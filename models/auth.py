from typing import Optional

from pydantic import BaseModel


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(User):
    password: str


class UserInDB(User):
    hashed_password: str
