from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, amount: Decimal):
        if amount < Decimal(0.00):
            raise ValueError("invalid amount for initial deposit.")
        self.balance = amount

    def __str__(self):
        return f"Name : {self.name}\nBalance : {self.balance}"
