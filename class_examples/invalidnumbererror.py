class InvalidNumberError(BaseException):
    def __init__(self):
        super().__init__("Invalid Number.")