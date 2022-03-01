from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from models.auth import User
from models.test import Test, TestResult, TestSubmission

router = APIRouter(
    prefix='/test',
    tags=['test'],
    dependencies=[Depends(get_current_user)],
)

@router.get('/', response_model=Test)
def get_test():
    ...


@router.post('/', response_model=TestResult)
def read_own_items(test_submission: TestSubmission,
                   user: User = Depends(get_current_user)):
    ...
