class Address:

    def __init__(self, city: str, country: str, houseNumber: str, street: str, state: str):
        self.state = state
        self.street = street
        self.houseNumber = houseNumber
        self.country = country
        self.city = city




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

    def test_that_accounts_could_be_deleted(self):
        bank: Bank = Bank()
        with self.assertRaises(ValueError) as error:
            bank.delete_account( "9090", "9086748927")
            self.assertTrue("mike jack Account does not exist." in error.exception)
