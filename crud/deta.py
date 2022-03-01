from deta import _Base

from exceptions import UserAlreadyExistsError
from models.auth import UserCreate, UserInDB
from services.auth import get_password_hash


def create_user(db: _Base, user: UserCreate):
    db_user = UserInDB(**user.dict(),
                       hashed_password=get_password_hash(user.password))
    try:
        db.insert(db_user.dict(), db_user.username)
    except Exception as err:
        if 'already exists' in str(err):
            raise UserAlreadyExistsError(db_user.username) from None
        raise
    return db_user


def get_user(db: _Base, username: str):
    user_dict = db.get(username)
    return UserInDB(**user_dict) if user_dict is not None else None
