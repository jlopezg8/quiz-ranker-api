from typing import Any, Dict

from exceptions import UserAlreadyExistsError
from models.auth import UserCreate, UserInDB
from services.auth import get_password_hash

DB = Dict[str, Dict[str, Any]]


def create_user(db: DB, user: UserCreate):
    if user.username in db_user:
        raise UserAlreadyExistsError(user.username)
    db_user = UserInDB(**user.dict(),
                       hashed_password=get_password_hash(user.password))
    db[db_user.username] = db_user.dict()
    return db_user


def get_user(db: DB, username: str):
    user_dict = db.get(username)
    return UserInDB(**user_dict) if user_dict is not None else None
