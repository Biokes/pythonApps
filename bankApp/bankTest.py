import pytest

from apps.bankApp.bank import Bank
from apps.bankApp.invalidNameError import AccountNotFoundError, InvalidPinError, InvalidAmountError


class TestBank:

    def test_bank_can_create_account(self):
        bank: Bank = Bank("UBA")
        bank.create_account("name", "9087")
        assert bank.number_of_customers() == 1

    def test_bank_find_accounts(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        assert bank.number_of_customers() == 1
        account_number = account.get_account_number()
        assert bank.find_account(account_number).get_account_number() == account_number

    def test_invalid_account_number_raises_error(self):
        bank: Bank = Bank("UBA")
        assert bank.number_of_customers() == 0
        account_number = 9087634323
        with pytest.raises(AccountNotFoundError) as info:
            bank.find_account(account_number)
        assert info.type == AccountNotFoundError

    def test_account_can_be_removed_with_correct_pin(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        assert bank.number_of_customers() == 1
        bank.remove_account(account.get_account_number(), "9087")
        assert bank.number_of_customers() == 0

    def test_accounts_can_be_removed_correct_pin(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account1 = bank.create_account("name", "9007")
        bank.create_account("name", "9067")
        assert bank.number_of_customers() == 3
        bank.remove_account(account.get_account_number(), "9087")
        assert bank.number_of_customers() == 2
        bank.remove_account(account1.get_account_number(), "9007")
        assert bank.number_of_customers() == 1

    def test_accounts_removal_with_wrong_pin_raises_error(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        bank.create_account("name", "9067")
        assert bank.number_of_customers() == 2
        bank.remove_account(account.get_account_number(), "9087")
        assert bank.number_of_customers() == 1
        with pytest.raises(AccountNotFoundError) as error:
            bank.remove_account(1234321234, "9087")
        assert error.type == AccountNotFoundError

    def test_bank_can_deposit(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        acc_num = account.get_account_number()
        bank.deposit(acc_num, 900)
        assert bank.check_balance(acc_num, "9087") == 900

    def test_invalid_account_for_deposit_raises_error(self):
        bank: Bank = Bank("UBA")
        with pytest.raises(AccountNotFoundError) as error:
            bank.deposit(8909876545, 900)
        assert error.type == AccountNotFoundError

    def test_invalid_pin_for_deposit_raises_error(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        acc_num = account.get_account_number()
        bank.deposit(acc_num, 900)
        bank.check_balance(acc_num, "9087")
        with pytest.raises(InvalidPinError) as error:
            bank.check_balance(acc_num, "9080")
        assert error.type == InvalidPinError

    def test_invalid_pin_does_not_affect_balance(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        acc_num = account.get_account_number()
        bank.deposit(acc_num, 900)
        bank.check_balance(acc_num, "9087")
        with pytest.raises(InvalidPinError) as error:
            bank.check_balance(acc_num, "9080")
        assert error.type == InvalidPinError
        assert bank.check_balance(acc_num, "9087") == 900

    def test_bank_can_deposit_multiple_accounts_andAllRunTransactions(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account1 = bank.create_account("name", "9085")
        account2 = bank.create_account("name", "9080")
        acc_num = account.get_account_number()
        acc_num1 = account1.get_account_number()
        acc_num2 = account2.get_account_number()
        bank.deposit(acc_num, 900)
        with pytest.raises(InvalidAmountError) as error:
            bank.deposit(acc_num1, -900)
        assert error.type == InvalidAmountError
        bank.check_balance(acc_num, "9087")
        with pytest.raises(InvalidPinError) as error:
            bank.check_balance(acc_num, "9080")
        assert error.type == InvalidPinError
        assert bank.check_balance(acc_num1, "9085") == 0
        assert bank.check_balance(acc_num, "9087") == 900
        with pytest.raises(InvalidAmountError) as error:
            bank.withdrawal(acc_num2, 900, "9080")
        assert error.type == InvalidAmountError

    def test_bank_can_transfer(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account_num = account.get_account_number()
        account1 = bank.create_account("name", "9085")
        bank.deposit(account_num, 500)
        account1_num = account1.get_account_number()
        assert bank.transfer(account_num, 500, account1_num, "9087") == "Transfer Successful."
        assert bank.check_balance(account_num, "9087") == 0
        assert bank.check_balance(account1_num, "9085") == 500

    def test_incorrect_account_number_raises_error(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account_num = account.get_account_number()
        with pytest.raises(AccountNotFoundError) as error:
            bank.transfer(9087890865, 200, account_num, "9008")
        assert error.type == AccountNotFoundError

    def test_incorrectPinCannotForTransfer_raisesError(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account_num = account.get_account_number()
        account1 = bank.create_account("name", "9085")
        bank.deposit(account_num, 500)
        account1_num = account1.get_account_number()
        with pytest.raises(InvalidPinError):
            bank.transfer(account_num, 500, account1_num, "9089")

    def test_incorrectPinForTransferRaisesError_balanceDoesNotChange(self):
        bank: Bank = Bank("UBA")
        account = bank.create_account("name", "9087")
        account_num = account.get_account_number()
        account1 = bank.create_account("name", "9085")
        bank.deposit(account_num, 500)
        account1_num = account1.get_account_number()
        with pytest.raises(InvalidPinError):
            bank.transfer(account_num, 500, account1_num, "9089")
        assert bank.check_balance(account_num, "9087") == 500
        assert bank.check_balance(account1_num, "9085") == 0
