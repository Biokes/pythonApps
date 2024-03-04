class InvalidCommandException(BaseException):
    def __init__(self):
        super().__init__("wrong command")

    def __init__(self, message):
        super().__init__(message)


class UnlockDiary(BaseException):
    def __init__(self):
        super().__init__("Diary is locked")
