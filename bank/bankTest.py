import unittest

from bank.account import Account
from bank.bank import Bank


class MyTestCase(unittest.TestCase):

    def test_That_account_could_be_added_to_list_of_account_in_bank(self):
        bank: Bank = Bank()
        acc: Account = Account("Gbadamosi taiwo", "9090", "9086748927")
        bank.add_to_list(acc)
        self.assertEqual(1, bank.number_of_accounts())

    def test_account_could_be_created(self):
        bank: Bank = Bank()
        name = "Gbadamosi taiwo"
        pin = "9090"
        account_number = "9086748927"
        acc: Account = Account("Gbadamosi taiwo", "9090", "9086748927")
        self.assertEqual(acc.name, bank.create_account(name, pin, account_number).name)

    def test_that_bank_deposit_to_account(self):
        bank: Bank = Bank()
        name = "Gbadamosi taiwo"
        pin = "9090"
        account_number = "9086748927"
        acc: Account = Account("Gbadamosi taiwo", "9090", "9086748927")
        self.assertEqual(acc.name, bank.create_account(name, pin, account_number).name)
        bank.deposit("9086748927", 500)
        self.assertEqual(500, bank.check_balance("9086748927", "9090"))

    def test_that_bank_cannot_deposit_to_account_that_does_not_exist(self):
        bank: Bank = Bank()
        name = "Gbadamosi taiwo"
        pin = "9090"
        account_number = "9086748927"
        acc: Account = Account("Gbadamosi taiwo", "9090", "9086748927")
        self.assertEqual(acc.name, bank.create_account(name, pin, account_number).name)
        with self.assertRaises(ValueError) as error:
            bank.deposit("9086748929", 500)
            self.assertTrue("Account Number: 9086748929 does not exist." in error.exception)


