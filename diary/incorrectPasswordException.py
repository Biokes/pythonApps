class IncorrectPasswordException(BaseException):
    def __init__(self):
        super().__init__("Incorrect password")
