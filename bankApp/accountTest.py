import pytest

from apps.bankApp.account_class import Account
from apps.bankApp.invalidNameError import InvalidAmountError, InvalidPinError


class TestAccount:
    def test_account_balance_is_zero_after_creating(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0.0

    def test_account_balance_increases_after_deposit(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0.0
        account.deposit(number, 500.0)
        assert account.check_balance(number, "9087") == 500

    def test_account_balance_is_zero_after_creation(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0.0

    def test_account_can_withdraw_and_deposit(self):
        account: Account = Account("name nam", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0.0
        account.deposit(number, 500.0)
        assert account.check_balance(number, "9087") == 500
        account.withdraw("9087", 500)
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500.0)
        assert account.check_balance(number, "9087") == 500

    def test_deposit_negative_amount_raises_error(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        with pytest.raises(InvalidAmountError) as info:
            account.deposit(number, -500.0)
        assert info.type == InvalidAmountError

    def test_proper_deposit_happens(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        with pytest.raises(InvalidAmountError) as info:
            account.deposit(number, -500.0)
        assert info.type == InvalidAmountError
        account.deposit(number, 500.0)
        assert account.check_balance(number, "9087") == 500
        account.withdraw("9087",  500)
        assert account.check_balance(number, "9087") == 0

    def test_account_can_withdraw(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        account.withdraw("9087", 200)

    def test_negative_withdrawal_raises_error(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        account.withdraw("9087", 200)
        assert account.check_balance(number, "9087") == 300

    def test_amount_greater_than_balance_raise_error(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw("9087", 700)
        assert info.type == InvalidAmountError

    def test_negative_amount_raises_error(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw("9087", -10)
        assert info.type == InvalidAmountError

    def test_that_incorrect_pin_throws_exception(self):
        account1: Account = Account("name name", "9080")
        number = account1.get_account_number()
        with pytest.raises(InvalidPinError) as info:
            assert account1.check_balance(number, "9087")
        assert info.type == InvalidPinError

    def test_transactions_can_happen_on_account(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw( "9087", -10)
        assert info.type == InvalidAmountError
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw("9087", 1700)
        assert info.type == InvalidAmountError

    def test_error_does_not_affect_balance(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw("9087", -10)
        assert info.type == InvalidAmountError
        account.deposit(number, 500)
        with pytest.raises(InvalidAmountError) as info:
            account.withdraw("9087", 1700)
        assert info.type == InvalidAmountError
        assert account.check_balance(number, "9087") == 1000

    def test_invalid_pin_cannot_be_used_to_withdraw(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidPinError) as error:
            account.withdraw("9088", 500)
        assert error.type == InvalidPinError

    def test_invalid_pin_for_withdrawal_does_not_affect_balance(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidPinError) as error:
            account.withdraw("9088", 500)
        assert error.type == InvalidPinError
        assert account.check_balance(number, "9087") == 500

    def test_invalid_pin_for_withdrawal_does_not_affect_account_transactions_that_can_be_done(self):
        account: Account = Account("name name", "9087")
        number = account.get_account_number()
        assert account.check_balance(number, "9087") == 0
        account.deposit(number, 500)
        with pytest.raises(InvalidPinError) as error:
            account.withdraw("9088", 500)
        assert error.type == InvalidPinError
        assert account.check_balance(number, "9087") == 500
        account.deposit(number, 500)
        account.withdraw("9087", 800)
        assert account.check_balance(number, "9087") == 200

