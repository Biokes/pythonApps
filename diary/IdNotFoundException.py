class IdNotFoundException(BaseException):
    def __init__(self):
        super().__init__("Id not found")
