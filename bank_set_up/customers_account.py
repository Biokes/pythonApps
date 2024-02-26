from bank_set_up.insufficientAmountException import InsufficientBalanceException
from bank_set_up.invalidAccountNumberException import InvalidAccountNumberException
from bank_set_up.invalidAmountException import InvalidAmountException
from bank_set_up.invalidPinException import InvalidPinException


class BankAccount:

    def validatePin(self, pin: str):
        if len(pin) != 4 or not pin.isnumeric():
            raise InvalidPinException("pls set a valid pin.")
        self.pin = pin
        pass

    def __init__(self, accountName: str, pin: str):
        self.accountName = accountName
        self.validatePin(pin)
        self.accountNumber = 0
        self.transactionRecords = []

    def checkAccountNumber(self) -> int:
        return self.accountNumber

    def deposit(self, number: int):
        if number < 0:
            raise InvalidAmountException("invalid deposit amount.")
        self.transactionRecords.append(number)
        pass

    def isCorrect(self, pin: str) -> bool:
        return self.pin == pin

    def checkBalance(self, pin: str) -> float:
        if not self.isCorrect(pin):
            raise InvalidPinException("Incorrect pin.")
        total = 0.0
        for transaction in self.transactionRecords:
            total += transaction
        return total

    def withdraw(self, amount: float, pin: str):
        if amount < 0:
            raise InvalidAmountException("Invalid Withdrawal Amount.")
        if self.checkBalance(pin) - amount < 0:
            raise InsufficientBalanceException("Insufficient balance.")
        if not self.isCorrect(pin):
            raise InvalidPinException("Incorrect Pin")
        self.transactionRecords.append(0 - amount)
        pass

    def validateAccountNumber(self, accountNumber: int):
        if len(str(accountNumber)) not in (10,):
            raise InvalidAccountNumberException("Invalid AccountNumber")
        self.accountNumber = accountNumber

    def setAccountNumber(self, accountNumber: int):
        self.validateAccountNumber(accountNumber)
        pass
