class InvalidCommandError(BaseException):
    def __init__(self):
        super().__init__("Invalid Username or Password.\n Pls check and retry.")


class UnlockDiary(BaseException):
    def __init__(self):
        super().__init__("Diary is locked")
