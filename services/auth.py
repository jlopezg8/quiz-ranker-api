from datetime import datetime, timedelta

from fastapi import Depends
from jose import jwt
from passlib.context import CryptContext

from config import settings
from data_access import Users
from models import User, UserCreate, UserInDB

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class AuthService:
    def __init__(self, users: Users = Depends()):
        self.users = users
    
    def authenticate_user(self, username: str, password: str):
        user = self.users.get(username)
        if user and pwd_context.verify(password, user.hashed_password):
            return user
        else:
            return None
    
    def create_access_token(self, user: User):
        exp_delta=timedelta(minutes=settings.access_token_expire_minutes)
        return jwt.encode(
            {
                'sub': user.username,
                'exp': datetime.utcnow() + exp_delta,
            },
            settings.secret_key,
            settings.algorithm
        )
    
    def create_user(self, user: UserCreate):
        pwd = pwd_context.hash(user.password)
        print(pwd)
        self.users.create(UserInDB(
            **user.dict(),
            hashed_password=pwd
        ))
    
    def get_user(self, username: str):
        return self.users.get(username)
