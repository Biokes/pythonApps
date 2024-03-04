class InvalidId(BaseException):
    def __init__(self):
        super().__init__("Invalid ID provided")
