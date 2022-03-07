from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from exceptions import UserAlreadyExistsError
from models import AccessToken, UserCreate
from services import AuthService

router = APIRouter(tags=['auth'])


@router.post(
    'login',
    response_model=AccessToken,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            'description': 'Incorrect username or password',
        },
    },
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth: AuthService = Depends()
):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return {
        'access_token': auth.create_access_token(user),
        'token_type': 'bearer',
    }


@router.post(
    'signup',
    response_model=AccessToken,
    responses={
        status.HTTP_409_CONFLICT: {
            'description': 'User already exists',
        },
    },
)
def signup(user: UserCreate, auth: AuthService = Depends()):
    try:
        auth.create_user(user)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already exists',
        )
    return {
        'access_token': auth.create_access_token(user),
        'token_type': 'bearer',
    }
