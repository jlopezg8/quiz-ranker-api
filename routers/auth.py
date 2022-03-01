from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from ..config import settings
from ..crud import authenticate_user, create_user
from ..database import get_users
from ..exceptions import UserAlreadyExistsError
from ..models.auth import Token, User, UserCreate
from ..services.auth import create_access_token

router = APIRouter(tags=['auth'])


@router.post('login', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    users = Depends(get_users)
):
    user = authenticate_user(users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return _create_token(user)


@router.post('signup', response_model=Token)
async def signup(user_create: UserCreate, users = Depends(get_users)):
    try:
        user = create_user(users, user_create)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists',
        )
    return _create_token(user)


def _create_token(user: User):
    access_token_expires = timedelta(
        minutes=settings.access_token_expire_minutes
    )
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
