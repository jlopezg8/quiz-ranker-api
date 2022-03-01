from config import settings
from services.auth import verify_password

if settings.environment == 'prod':
    from crud.deta import *
else:
    from crud.dict import *


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
