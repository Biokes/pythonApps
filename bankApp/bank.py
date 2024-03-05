from apps.bankApp.account_class import Account
from apps.bankApp.invalidNameError import AccountNotFoundError


class Bank:

    def create_account(self, name: str, pin: str):
        account = Account(name, pin)
        self.customers.append(account)
        return account.__str__()

    def number_of_customers(self) -> int:
        return len(self.customers)

    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self.customers = []

    def find_account(self, account_number: int) -> Account:
        for account in self.customers:
            if account.get_account_number() == account_number:
                return account
        raise AccountNotFoundError

    def remove_account(self, account_number: int, pin: str):
        if self.find_account(account_number).check_pin(pin):
            self.customers.remove(self.find_account(account_number))
            return "Account Deleted Successfully."
        raise AccountNotFoundError

    def deposit(self, acc_num: int, amount: float):
        self.find_account(acc_num).deposit(acc_num, amount)
        return "Successful deposit."

    def check_balance(self, acc_num: int, pin: str):
        account: Account = self.find_account(acc_num)
        return account.get_balance(pin)

    def withdrawal(self, acc_number: int, amount: float, pin: str):
        self.find_account(acc_number).withdraw(pin, amount)
        return "Withdraw Successful."

    def transfer(self, sender_account: int, amount: float, receiver_account: int, pin: str):
        self.withdrawal(sender_account, amount, pin)
        self.deposit(receiver_account, amount)
        return "Transfer Successful."

