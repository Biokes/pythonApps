class InvalidPinException(Exception):
    def __init__(self, errorMessage: str):
        super().__init__(errorMessage)
