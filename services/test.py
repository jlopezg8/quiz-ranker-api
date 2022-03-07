from fastapi import Depends

from data_access import Test


class TestService:
    def __init__(self, test: Test = Depends()):
        self.test = test
    
    def get_test(self):
        return self.test.get()
