from fastapi import Depends

from data_access import Test
from models import TestResult, TestSubmission


class TestService:
    def __init__(self, test: Test = Depends()):
        self.test = test
    
    def get_test(self):
        return self.test.get()

    def submit_test(self, test_submission: TestSubmission):
        return TestResult(result='G1')
