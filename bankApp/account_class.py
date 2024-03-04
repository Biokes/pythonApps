import secrets

from apps.bankApp.invalidNameError import InvalidAccountNumberError, InvalidPinError, InvalidAmountError, \
    InvalidNameError


class Account:

    def validatePin(self, pin):
        if not pin.isnumeric() or len(pin) != 4:
            raise InvalidPinError
        self.pin = pin

    def validate_name(self, name: str):
        if not name:
            raise InvalidNameError
        self.name = name


    def __init__(self, name: str, pin: str):
        self._balance = 0.0
        self.validatePin(pin)
        self.validate_name(name)
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        account_number_generated = secrets.randbelow(1299768789)
        if account_number_generated < 1000009999:
            self.generate_account_number()
        return account_number_generated

    def get_account_number(self) -> int:
        return self.account_number

    def deposit(self, account_given: int, value: float):
        if value < 0:
            raise InvalidAmountError
        if account_given == self.account_number:
            self._balance += value
            pass

    def check_balance(self, number_given: int, pin_given: str):
        if self.pin == pin_given:
            if self.account_number == number_given:
                return self._balance
            raise InvalidAccountNumberError
        raise InvalidPinError

    def withdraw(self, pin: str, withdraw_amount):
        if self.pin != pin:
            raise InvalidPinError
        if withdraw_amount > self._balance:
            raise InvalidAmountError
        if withdraw_amount <= 0:
            raise InvalidAmountError
        self._balance -= withdraw_amount
        return

    def check_pin(self, pin: str):
        return self.pin == pin

    def get_balance(self, pin):
        if self.pin == pin:
            return self._balance
        raise InvalidPinError

