class InvalidCommandError(BaseException):
    def __init__(self):
        super().__init__("Invalid name or password.")


class UnlockDiary(BaseException):
    def __init__(self):
        super().__init__("Diary is locked")
