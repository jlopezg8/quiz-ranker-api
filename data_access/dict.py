from exceptions import UserAlreadyExistsError
from models import Question, Test as TestModel, UserInDB

_questions = [
    {
        'key': '1',
        'question': 'Q1',
        'choices': ['C1', 'C2', 'C3', 'C4'],
        'correct_answer_index': 0,
    },
    {
        'key': '2',
        'question': 'Q2',
        'choices': ['C1', 'C2', 'C3', 'C4'],
        'correct_answer_index': 2,
    },
    {
        'key': '3',
        'question': 'Q3',
        'choices': ['C1', 'C2', 'C3', 'C4'],
        'correct_answer_index': 1,
    },
]


class Test:    
    def get(self):
        questions = [Question(**question) for question in _questions]
        return TestModel(questions=questions)


_users = {
    'user1': {
        'username': 'user1',
        'full_name': 'user1',
        'email': 'user1@example.com',
        'hashed_password': '$2b$12$5pnpbMIhWfRGQzMh0wCYh.18a6esBVsfAa5p45jyRIs8wowen6wH2',
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
