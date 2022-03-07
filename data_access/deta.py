from deta import Deta, _Base
from fastapi import Depends

from exceptions import UserAlreadyExistsError
from models import UserInDB

# While using our SDKs(the latest versions) within a Deta Micro, you can omit
# specifying the project key when instantiating a service instance.
_deta = Deta(
    #'project key'
)


def _get_users():
    # This how to connect to or create a database.
    # You can create as many as you want without additional charges.
    return _deta.Base('users')


class Users:
    def __init__(self, db: _Base = Depends(_get_users)):
        self.db = db

    def get(self, username: str):
        user_dict = self.db.get(username)
        return UserInDB(**user_dict) if user_dict is not None else None

    def create(self, user: UserInDB):
        try:
            self.db.insert(user.dict(), user.username)
        except Exception as err:
            if 'already exists' in str(err):
                raise UserAlreadyExistsError(user.username) from None
            raise
