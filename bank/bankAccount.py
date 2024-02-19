from bank.customersAccount import BankAccount


class Bank:
    def __init__(self):
        self.list_of_accounts = []

    def add_to_list(self, acc: BankAccount):
        self.list_of_accounts.append(acc)
        pass

    def number_of_accounts(self):
        return len(self.list_of_accounts)

    def create_account(self, name: str, pin: str, account_number: str):
        acc: BankAccount = BankAccount(name, pin, account_number)
        newAcc = [acc, account_number]
        self.list_of_accounts.append(newAcc)
        return acc

    def deposit(self, account_number: str, amount: float):
        for items in self.list_of_accounts:
            if items[1] == account_number:
                items[0].deposit(amount, account_number)
            else:
                raise ValueError(f"user: {account_number} does not exist.")

    def check_balance(self, account_number: str, pin: str):
        for items in self.list_of_accounts:
            if items[1] == account_number:
                return items[0].balance(pin, account_number)
            else:
                raise ValueError(f"Account Number: {account_number} does not exist.")
