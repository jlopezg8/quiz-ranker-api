from http import HTTPStatus
from urllib.error import HTTPError

from deta import Deta, _Base
from fastapi import Depends

from config import settings
from exceptions import UserAlreadyExistsError
from models import Question, Test as TestModel, UserInDB

# While using our SDKs(the latest versions) within a Deta Micro, you can omit
# specifying the project key when instantiating a service instance.
_deta = Deta(
    settings.deta_project_key
)


def _get_test():
    # This how to connect to or create a database.
    # You can create as many as you want without additional charges.
    return _deta.Base('test')


class Test:
    def __init__(self, db: _Base = Depends(_get_test)):
        self.db = db

    def get(self):
        questions_dicts = self.db.fetch().items
        questions = [Question(**question) for question in questions_dicts]
        return TestModel(questions=questions)


def _get_users():
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
        except HTTPError as err:
            if err.code == HTTPStatus.CONFLICT:
                raise UserAlreadyExistsError(user.username) from None
            raise
