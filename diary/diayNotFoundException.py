class DiaryNotFoundError(BaseException):
    def __init__(self):
        super().__init__("Diary with username provided does not exist")
