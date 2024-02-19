from bankAccount import BankAccount


class TestBankAccount:
    def test_deposit5k_balanceIs5k(self):
        account: BankAccount = BankAccount("name lastName", "8923")
        account.deposit(5000)
        assert account.checkBalance("8923") == 5000
