import sys

from apps.bankApp.bank import Bank
from apps.bankApp.invalidNameError import InvalidPinError, InvalidNameError, InvalidAmountError, \
    InvalidAccountNumberError


class BankApp:

    def __init__(self, name: str):
        self.bank = Bank(name)

    def home_page(self):
        try:
            option = self.menu_page()
            self.menu(option)
        except KeyboardInterrupt as error:
            print("idiot u wan break code abi😒😒😒😒😒😒.")
        except BaseException:
            print("Something went Wrong.")
        finally:
            self.home_page()

    def menu_page(self):
        option = int(input("""
welcome to Mavericks Bank🤭🤭🤭
1. create account
2. Deposit
3. Withdraw
4. Transfer
5. check Balance
6. Close Account
7. Exit
Enter your choice: """))

        return option

    def case_one(self):
        try:
            name = input("Enter your full name: ")
            pin = input("Enter your preferred pin: ")
            print(
                f"Account created successfully\nyour account Number is "
                f"{self.bank.create_account(name, pin).get_account_number()}")
        except InvalidPinError as e:
            print(f"{e}")
        except InvalidNameError as e:
            print(f"{e}")
        finally:
            self.home_page()

    def case_two(self):
        try:
            acc_number = int(input("Enter account to deposit: "))
            amount = float(input("Enter amount: "))
            self.bank.deposit(acc_number, amount)
        except InvalidAmountError as error:
            print(error)
        except InvalidAccountNumberError as error:
            print(error)
        finally:
            self.home_page()

    def case_three(self):
        try:
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount: "))
            pin = input("Enter your pin: ")
            self.bank.withdraw(acc_number, amount, pin)
        except InvalidAmountError as error:
            print(f"{error}")
        except InvalidAccountNumberError as error:
            print(f'{error}')
        except InvalidPinError as error:
            print(f'{error}')
        finally:
            self.home_page()

    def case_four(self):
        try:
            sender = int(input("Enter sender's account Number: "))
            receiver = int(input("Enter the receiver's account: "))
            pin = input("Enter your pin: ")
            amount = float(input("Enter amount: "))
            self.bank.transfer(sender, amount, receiver, pin)
        except InvalidPinError as error:
            print(f"{error}")
        except InvalidAccountNumberError as error:
            print(f'{error}')
        except InvalidAmountError as error:
            print(f'{error}')
        finally:
            self.home_page()

    def case_five(self):
        try:
            account_number = int(input("Enter your Account Number: "))
            pin = input("Enter your pin: ")
            print(self.bank.check_balance(account_number, pin))
        except InvalidPinError:
            print("Invalid pin Entered")
        except InvalidAccountNumberError:
            print("Account not found")
        finally:
            self.home_page()

    def case_six(self):
        try:
            account_number = int(input("Enter the account number you want to remove: "))
            pin = input("Enter your pin: ")
            account = self.bank.find_account(account_number)
            if account.check_balance(account_number, pin) == 0:
                choice = input(f"You still have {account.check_balance(account_number, pin)} in your balance\n"
                               f"1. continue to delete\n2. Main menu")
                match choice:
                    case "1":
                        account_number = int(input("Enter the account number you want to remove: "))
                        pin = input("Enter your pin: ")
                        self.bank.remove_account(account_number, pin)
                    case 2:
                        self.menu(3)
            self.bank.remove_account(account_number, pin)
        except InvalidPinError as error:
            print(f"{error}")
        except InvalidAccountNumberError as error:
            print(f'{error}')
        except InvalidAmountError as error:
            print(f'{error}')
        finally:
            self.home_page()

    def main_menu(self):
        choice = input("welcome To mavericks bank.\n1. create Account\n2. Exit App\nEnter your choice:  ")
        match choice:
            case"1":
                self.case_one()
            case"2":
                sys.exit(0)
            case _:
                self.main_menu()

    # @tryBlock
    def menu(self, choice: int):
        self.main_menu()
        match choice:
            case 1:
                self.case_one()
            case 2:
                self.case_two()
            case 3:
                self.case_three()
            case 4:
                self.case_four()
            case 5:
                self.case_five()
            case 6:
                self.case_six()

            case 7:
                print("GoodBye😘😘😘")
                sys.exit()


if __name__ == '__main__':
    bankApp = BankApp("Mavericks Bank")
    bankApp.main_menu()
