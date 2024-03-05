class NameAlreadyExistError(BaseException):
    def __init__(self):
        super().__init__("Name Already Exist.")
