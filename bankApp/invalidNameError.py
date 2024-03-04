class InvalidAccountNumberError(BaseException):
    def __init__(self):
        super().__init__("Invalid Account")


class InvalidPinError(BaseException):
    def __init__(self):
        super().__init__("Invalid pin.")


class InvalidAmountError(BaseException):
    def __init__(self):
        super().__init__("Invalid Amount.")


class AccountNotFoundError(BaseException):
    def __init__(self):
        super().__init__("Account not found Error.")


class InvalidNameError(BaseException):
    def __init__(self):
        super().__init__("Invalid Name.")
