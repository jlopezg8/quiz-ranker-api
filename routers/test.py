from fastapi import APIRouter, Depends

from dependencies import get_current_user
from models import Test, TestResult, TestSubmission
from services import TestService

router = APIRouter(
    tags=['test'],
    dependencies=[Depends(get_current_user)],
)

@router.get('/get_test', response_model=Test)
def get_test(test: TestService = Depends()):
    return test.get_test()


@router.post('/submit_test', response_model=TestResult)
def submit_test(test_submission: TestSubmission):
    ...
