from typing import List

from pydantic import BaseModel


class Question(BaseModel):
    question: str
    choices: List[str]
    correct_answer: str


class Test(BaseModel):
    questions: List[Question]


class Answer(BaseModel):
    question: str
    answer: str


class TestSubmission(BaseModel):
    answers: List[Answer]


class TestResult(BaseModel):
    result: str
