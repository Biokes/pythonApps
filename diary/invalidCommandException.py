class InvalidCommandException(BaseException):
    def __init__(self):
        super().__init__("wrong command")
