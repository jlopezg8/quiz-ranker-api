class UserAlreadyExistsError(ValueError):
    def __init__(self, username):
        super().__init__(f'User with username "{username}" already exists')
