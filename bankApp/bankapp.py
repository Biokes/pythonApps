import sys

from apps.bankApp.bank import Bank
from apps.bankApp.invalidNameError import *
import tkinter as display
from tkinter import simpledialog, messagebox


class BankApp:

    def __init__(self, name: str):
        self.bank = Bank(name)
        self.root = display.Tk()
        self.root.withdraw()

    def create_account(self):
        try:
            full_name = simpledialog.askstring("Create Account Menu", "Enter your full name")
            pin = simpledialog.askstring("Create Account Menu", "Enter your preferred pin")
            account = self.bank.create_account(full_name, pin)
            messagebox.showwarning("Successful", f"Account Successfully registered\n"
                                                 f"{account}")
        except InvalidPinError:
            messagebox.showwarning("warning", f"Invalid pin\nPin must be 4 digits")
            self.create_account()
        except InvalidNameError as e:
            messagebox.showwarning("warning", "Invalid name.")
            self.create_account()

    def welcome_page(self):
        response = simpledialog.askstring("Welcome page.",
                                          "    Welcome to Mavericks bank\n 1. create Account.\n2. Exit")
        match response:
            case "1":
                self.create_account()
            case "2":
                messagebox.showwarning("Exit", "Exiting............")
                sys.exit(0)
            case _:
                messagebox.showwarning("Warning", "You entered an invalid option.")
                self.welcome_page()

    def deposit(self):
        try:
            acc_number = simpledialog.askinteger("Deposit", "Enter account number to deposit: ")
            amount = simpledialog.askfloat("Deposit", "Enter a valid amount to deposit: ")
            self.bank.deposit(acc_number, amount)
            print("Successful deposit\n\n")
        except InvalidAmountError as error:
            messagebox.showwarning("Warning", f"{error}.")
            self.deposit()
        except InvalidAccountNumberError as error:
            print(error)
            self.deposit()
        except ValueError:
            print("Something went wrong.")
            self.deposit()

    def main_menu(self):
        option = simpledialog.askstring("Home page", """
                                welcome to Mavericks Bank🤭🤭🤭
                                1. create account
                                2. Deposit
                                3. Withdraw
                                4. Transfer
                                5. check Balance
                                6. Close Account
                                7. Exit""")
        match option:
            case "1":
                self.create_account()
            case "2":
                self.deposit()
            case _:
                messagebox.showwarning("Error", "Wrong input\nselect form 1-7")
                self.main_menu()


#     def landing_page(self):
#         choice = simpledialog.askstring("Welcome Message",
#                                         "welcome To mavericks bank.\n1. create Account\n2. Exit App\nEnter your "
#                                         "choice:  ")
#         match choice:
#             case "1":
#                 self.create_account()
#             case "2":
#                 sys.exit()
#             case _:
#                 self.landing_page()
#
#     def home_page(self):
#         try:
#             option = self.full_display_menu()
#             self.full_display(option)
#         except KeyboardInterrupt as error:
#             print(f"{error}\nidiot u wan break code abi😒😒😒😒😒😒.")
#         except Exception:
#             print("idiot u wan break code abi😒😒😒😒😒😒.")
#         finally:
#             self.home_page()
#
#
#     def full_display_menu(self):
#         return option
#
#
#
#     def case_two(self):
#
#         finally:
#             self.full_display(self.full_display_menu())
#
#     def case_three(self):
#         try:
#             print("\n\n<<<<<<<<Withdraw Menu>>>>>>>>>>\n\n")
#             acc_number = int(input("Enter account number: "))
#             amount = float(input("Enter amount: "))
#             pin = input("Enter your pin: ")
#             print(self.bank.withdrawal(acc_number, amount, pin))
#             self.full_display_menu()
#         except InvalidAmountError as error:
#             print(error)
#             self.case_three()
#         except InvalidAccountNumberError as error:
#             print(error)
#             self.case_three()
#         except InvalidPinError as error:
#             print(error)
#             self.case_three()
#         finally:
#             self.full_display(self.full_display_menu())
#
#     def case_four(self):
#         try:
#             print("\n\n<<<<<<<Transfer Menu>>>>>>>>>")
#             sender = int(input("Enter sender's account Number: "))
#             receiver = int(input("Enter the receiver's account: "))
#             pin = input("Enter your pin: ")
#             amount = float(input("Enter amount: "))
#             print(self.bank.transfer(sender, amount, receiver, pin))
#         except InvalidPinError as error:
#             print(error)
#             self.full_display(self.full_display_menu())
#         except InvalidAccountNumberError as error:
#             print(error)
#             self.full_display(self.full_display_menu())
#         except InvalidAmountError as error:
#             print(error)
#             self.full_display(self.full_display_menu())
#         except AccountNotFoundError as error:
#             print(error)
#             self.full_display(self.full_display_menu())
#         finally:
#             self.full_display(self.full_display_menu())
#
#     def case_five(self):
#         try:
#             print("\n\n<<<<<<<<<<Check Balance Menu>>>>>>>>>\n\n")
#             account_number = int(input("Enter your Account Number: "))
#             pin = input("Enter your pin: ")
#             print("Account Balance: $" + self.bank.check_balance(account_number, pin))
#         except InvalidPinError as error:
#             print(f"{error}")
#             self.full_display(self.full_display_menu())
#         except InvalidAccountNumberError as error:
#             print(f"{error}")
#             self.full_display(self.full_display_menu())
#         except InvalidAmountError as error:
#             print(f"{error}")
#             self.full_display(self.full_display_menu())
#         except AccountNotFoundError as error:
#             print(f"{error}")
#             self.full_display(self.full_display_menu())
#         finally:
#             self.full_display(self.full_display_menu())
#
#     def case_six(self):
#         try:
#             account_number = int(input("Enter the account number you want to remove: "))
#             pin = input("Enter your pin: ")
#             account = self.bank.find_account(account_number)
#             if account.check_balance(account_number, pin) == 0:
#                 choice = input(f"You still have {account.check_balance(account_number, pin)} in your balance\n"
#                                f"1. continue to delete\n2. Main menu")
#                 match choice:
#                     case "1":
#                         account_number = int(input("Enter the account number you want to remove: "))
#                         pin = input("Enter your pin: ")
#                         self.bank.remove_account(account_number, pin)
#                     case 2:
#                         self.full_display(3)
#                     case _:
#                         print("😒😒😒Wrong Input.\n\n")
#                         self.case_six()
#             self.bank.remove_account(account_number, pin)
#             print("Account removed Successfully.\n\n")
#         except InvalidPinError as error:
#             print(f"{error}")
#             self.case_six()
#         except InvalidAccountNumberError as error:
#             print(f"{error}")
#             self.case_six()
#         except InvalidAmountError as error:
#             print(f"{error}")
#             self.case_six()
#         finally:
#             self.full_display(self.full_display_menu())
#
#     def full_display(self, choice: int):
#         match choice:
#             case 1:
#                 self.create_account()
#             case 2:
#                 self.case_two()
#             case 3:
#                 self.case_three()
#             case 4:
#                 self.case_four()
#             case 5:
#                 self.case_five()
#             case 6:
#                 self.case_six()
#             case 7:
#                 print("GoodBye😘😘😘")
#                 sys.exit()
#             case _:
#                 print("🤦‍♂️🤦‍♂️🤦‍♂️🤦‍♂️\nWrong Input.")
#                 self.full_display(self.full_display_menu())
#
#


if __name__ == '__main__':
    bankApp = BankApp("Mavericks Bank")
    bankApp.welcome_page()
