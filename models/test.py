from typing import List

from pydantic import BaseModel


class Question(BaseModel):
    key: str
    question: str
    choices: List[str]
    correct_answer_index: int


class Test(BaseModel):
    questions: List[Question]


class Answer(BaseModel):
    question_key: str
    answer_index: int


class TestSubmission(BaseModel):
    answers: List[Answer]


class TestResult(BaseModel):
    result: str
