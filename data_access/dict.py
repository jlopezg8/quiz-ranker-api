from typing import Any, Dict

from exceptions import UserAlreadyExistsError
from models import UserInDB

DB = Dict[str, Dict[str, Any]]

_users: DB = {
    'johndoe': {
        'username': 'johndoe',
        'full_name': 'John Doe',
        'email': 'johndoe@example.com',
        'hashed_password': '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW',
        'disabled': False,
    }
}


class Users:    
    def get(self, username: str):
        user_dict = _users.get(username)
        return UserInDB(**user_dict) if user_dict is not None else None
    
    def create(self, user: UserInDB):
        if user.username in _users:
            raise UserAlreadyExistsError(user.username)
        _users[user.username] = user.dict()
