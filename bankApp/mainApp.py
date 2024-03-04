import sys

from apps.bankApp.bank import Bank
from apps.bankApp.invalidNameError import *


class BankApp:

    def __init__(self, name: str):
        self.bank = Bank(name)

    def landing_page(self):
        choice = input("welcome To mavericks bank.\n1. create Account\n2. Exit App\nEnter your choice:  ")
        match choice:
            case"1":
                self.case_one()
            case"2":
                sys.exit()
            case _:
                self.landing_page()

    def home_page(self):
        try:
            option = self.full_display_menu()
            self.full_display(option)
        except KeyboardInterrupt as error:
            print(f"{error}\nidiot u wan break code abi😒😒😒😒😒😒.")
        except Exception:
            print("idiot u wan break code abi😒😒😒😒😒😒.")
        finally:
            self.home_page()

    @classmethod
    def full_display_menu(cls):
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
            print("\n\n<<<<<<<<<<Create Account Menu>>>>>>>>>>>\n")
            name = input("Enter your full name: ")
            pin = input("Enter your preferred pin: ")
            print(
                f"Account created successfully\nyour account Number is "
                f"{self.bank.create_account(name, pin).get_account_number()}")
        except InvalidPinError as e:
            print(f"{e}")
            self.case_one()
        except InvalidNameError as e:
            print(f"{e}")
            self.case_one()
        finally:
            self.home_page()

    def case_two(self):
        try:
            print("\n\n<<<<<<<<Deposit Menu.>>>>>>>>>>\n\n")
            acc_number = int(input("Enter account to deposit: "))
            amount = float(input("Enter amount: "))
            self.bank.deposit(acc_number, amount)
            print("Successful deposit\n\n")
        except InvalidAmountError as error:
            print(error)
            self.case_two()
        except InvalidAccountNumberError as error:
            print(error)
            self.case_two()
        except Exception:
            print("Something went wrong.")
            self.case_two()
        finally:
            self.full_display(self.full_display_menu())

    def case_three(self):
        try:
            print("\n\n<<<<<<<<Withdraw Menu>>>>>>>>>>\n\n")
            acc_number = int(input("Enter account number: "))
            amount = float(input("Enter amount: "))
            pin = input("Enter your pin: ")
            print(self.bank.withdrawal(acc_number, amount, pin))
            self.full_display_menu()
        except InvalidAmountError as error:
            print(error)
            self.case_three()
        except InvalidAccountNumberError as error:
            print(error)
            self.case_three()
        except InvalidPinError as error:
            print(error)
            self.case_three()
        finally:
            self.full_display(self.full_display_menu())

    def case_four(self):
        try:
            print("\n\n<<<<<<<Transfer Menu>>>>>>>>>")
            sender = int(input("Enter sender's account Number: "))
            receiver = int(input("Enter the receiver's account: "))
            pin = input("Enter your pin: ")
            amount = float(input("Enter amount: "))
            print(self.bank.transfer(sender, amount, receiver, pin))
        except InvalidPinError as error:
            print(error)
            self.full_display(self.full_display_menu())
        except InvalidAccountNumberError as error:
            print(error)
            self.full_display(self.full_display_menu())
        except InvalidAmountError as error:
            print(error)
            self.full_display(self.full_display_menu())
        except AccountNotFoundError as error:
            print(error)
            self.full_display(self.full_display_menu())
        finally:
            self.full_display(self.full_display_menu())

    def case_five(self):
        try:
            print("\n\n<<<<<<<<<<Check Balance Menu>>>>>>>>>\n\n")
            account_number = int(input("Enter your Account Number: "))
            pin = input("Enter your pin: ")
            print("Account Balance: $" + self.bank.check_balance(account_number, pin))
        except InvalidPinError as error:
            print(f"{error}")
            self.full_display(self.full_display_menu())
        except InvalidAccountNumberError as error:
            print(f"{error}")
            self.full_display(self.full_display_menu())
        except InvalidAmountError as error:
            print(f"{error}")
            self.full_display(self.full_display_menu())
        except AccountNotFoundError as error:
            print(f"{error}")
            self.full_display(self.full_display_menu())
        finally:
            self.full_display(self.full_display_menu())

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
                        self.full_display(3)
                    case _:
                        print("😒😒😒Wrong Input.\n\n")
                        self.case_six()
            self.bank.remove_account(account_number, pin)
            print("Account removed Successfully.\n\n")
        except InvalidPinError as error:
            print(f"{error}")
            self.case_six()
        except InvalidAccountNumberError as error:
            print(f"{error}")
            self.case_six()
        except InvalidAmountError as error:
            print(f"{error}")
            self.case_six()
        finally:
            self.full_display(self.full_display_menu())

    def full_display(self, choice: int):
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
            case _:
                print("🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️\nWrong Input.")
                self.full_display(self.full_display_menu())


if __name__ == '__main__':
    bankApp = BankApp("Mavericks Bank")
    bankApp.landing_page()
