import unittest
from decimal import Decimal

from bank.account import Account


class MyTestCase(unittest.TestCase):
    def test_that_user_can_set_pin(self):
        account: Account = Account("baba mama", "4903", "90834758937")
        self.assertEqual(Decimal(0), account.balance("4903", "90834758937"))

    def test_that_user_can_deposit(self):
        account: Account = Account("baba mama", "4903", "90834758937")
        self.assertEqual(0, account.balance("4903", "90834758937"))
        account.deposit(900, "90834758937")
        self.assertEqual(900, account.balance("4903", "90834758937"))

    def test_that_user_can_withdraw(self):
        account: Account = Account("baba mama", "4903", "90834758937")
        self.assertEqual(0, account.balance("4903", "90834758937"))
        account.deposit(900, "90834758937")
        self.assertEqual(900, account.balance("4903", "90834758937"))
        account.withdraw(500, "4903", "90834758937")
        self.assertEqual(400, account.balance("4903", "90834758937"))

    def test_that_user_cannot_withdraw_all_balance(self):
        account: Account = Account("baba mama", "4903", "90834558937")
        self.assertEqual(0, account.balance("4903", "90834558937"))
        account.deposit(900, "90834558937")
        self.assertEqual(900, account.balance("4903", "90834558937"))
        account.withdraw(900, "4903", "90834558937")
        self.assertEqual(0, account.balance("4903", "90834558937"))

    def test_that_user_cannot_withdraw_more_than_balance(self):
        acc: Account = Account("bada mama", "9808", "0897094859")
        with self.assertRaises(ValueError) as context:
            acc.withdraw(900, "9808", "0897094859")
            self.assertTrue("withdrawal amount must be greater than 0.0 and less than or equal to balance" in context.exception)
        self.assertEqual(0, acc.balance("9808", "0897094859"))
        acc.deposit(900, "0897094859")
        self.assertEqual(900, acc.balance("9808", "0897094859"))

    def test_that_account_cannot_be_used_if_not_created(self):
        acc: Account = Account("bada mama", "9808", "0897094859")
        with self.assertRaises(ValueError) as context:
            acc.withdraw(900, "9808", "0897094790")
            self.assertTrue("User 0897094790 does not Exist." in context.exception)
