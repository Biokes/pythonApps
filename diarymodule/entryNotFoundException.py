class EntryNotFoundError(BaseException):
    def __init__(self):
        super().__init__("No Entry id matches provided id.")
