class Account:

    def __init__(self, name: str, pin: str, number: str,):
        self.name = name
        self.transaction_history = [0.0]
        if not pin.isnumeric() and len(pin) != 4:
            raise ValueError("Invalid pin\nPin must be 4 digits.")
        else:
            self.pin = pin
        if not number.isnumeric() and len(number) != 10:
            raise ValueError("Invalid number\nNumber must be 11 digits.")
        else:
            self.account_number = number

    @property
    def name(self, name: str):
        self.name = name

    @name.setter
    def name(self, value):
        self._name = value

    @name.getter
    def name(self):
        return sum(self.transaction_history)

    def deposit(self, amount: float, account_number: str):
        if amount < 0.0:
            raise ValueError("Deposit must  be greater than 0.0")
        self.transaction_history.append(amount)
        if account_number != self.account_number:
            raise ValueError(f"User {account_number} does not Exist.")

    def withdraw(self, amount: float, pin: str, account_number: str):
        if amount < 0.0 or amount > sum(self.transaction_history):
            raise ValueError("withdrawal amount must be greater than 0.0 and less than or equal to balance")
        if pin != self.pin:
            raise ValueError("Incorrect pin")
        self.transaction_history.append(0-amount)
        if account_number != self.account_number:
            raise ValueError(f"User {account_number} does not Exist.")
        return "Successful Withdrawal."

    def change_pin(self, pin: str):
        if pin != self.pin:
            raise ValueError("Incorrect pin.")
        self.pin = pin

    def balance(self, pin: str, acc_number: str):
        if self.pin != pin:
            raise ValueError("Incorrect pin.")
        if acc_number != self.account_number:
            raise ValueError(f"User {acc_number} does not Exist.")
        return sum(self.transaction_history)



