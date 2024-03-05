class InvalidId(BaseException):
    def __init__(self):
        super().__init__("Invalid ID provided")


class UsernameNotFound(BaseException):
    def __init__(self):
        super().__init__("Username provided does not match any username.")
