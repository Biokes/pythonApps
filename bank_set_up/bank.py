
from bank_set_up.customers_account import BankAccount
from bank_set_up.invalidAccountNumberException import InvalidAccountNumberException





class Bank:
    def __init__(self, bankName: str):
        self.bankName = bankName
        self.customers = []
        self.countUsers = 1009876543

    def addNewAccount(self, customerAccount: BankAccount ):
        self.customers.append(customerAccount)

    def numberOfCustomers(self):
        return len(self.customers)

    def deposit(self, accountNumber: int,depositAmount: float):
        for acc in self.customers:
            if accountNumber == acc.checkAccountNumber():
                acc.deposit(depositAmount)
                return
        errorMessage = f"Account number: {accountNumber} does not Exist."
        raise InvalidAccountNumberException(errorMessage)

    def checkBalance(self, accountNumber:int,pin: str):
        for accounts in self.customers:
            if accountNumber == accounts.checkAccountNumber():
                return accounts.checkBalance(pin)
        raise InvalidAccountNumberException();

# }
#
# public
# void
# withdraw(int
# accountNumber, double
# withdrawalAmount, String
# pin)
# throws
# InvalidAmountException, IncorrectAccountNumberException, InsufficientBalanceException
# {
# for (BankAccount account: customers)
#     if (accountNumber == account.checkAccountNumber()) {
#     account.withdraw(withdrawalAmount, pin);
#     return;
#     }
#     throw
#     new
#     IncorrectAccountNumberException("Invalid Account number.");
#     }
#
#     public
#     void
#     transfer(int
#     senderAccountNumber, int
#     receiverAccountNumber, double
#     amount, String
#     senderPin)
#     throws
#     IncorrectAccountNumberException, InvalidAmountException, InsufficientBalanceException
#     {
#         boolean
#     breaker = false;
#     for (int count = 0; count < customers.size();count++) {
#     if (customers.get(count).checkAccountNumber() == senderAccountNumber) {
#     for (int counter = 0; counter < customers.size(); counter++) {
#     if ( customers.get(counter).checkAccountNumber() == receiverAccountNumber) {
#     customers.get(count).withdraw(amount, senderPin);
#     customers.get(counter).deposit(amount);
#     breaker = true;
#     }
#     }
#     }
#
# }
# }
#
# public
# BankAccount
# registerCustomer(String
# firstName, String
# lastName, String
# pin){
#     BankAccount
# account = new
# BankAccount(String.format("%s %s", firstName, lastName), pin);
# account.setAccountNumber(generateAccountNumber());
# customers.add(account);
# return account;
# }
# private
# int
# generateAccountNumber()
# {
# return countUsers + numberOfCustomers() + 1;
#
# }
# public
# void
# removeAccount(int
# accountNumber, String
# pin) throws
# IncorrectAccountNumberException
# {
# for (BankAccount acc: customers){
# if (acc.checkAccountNumber() == accountNumber) {
# if (!acc.isCorrect(pin)){
# throw new InvalidPinException("incporrect pin.");
# }
# customers.remove(acc);
# return;
# }
# }
#
# throw
# new
# InvalidPinException("Incorrect account Number");
#
# }
#
# public
# BankAccount
# findAccount(int
# accountNumber)throws
# IncorrectAccountNumberException
# {
# for (BankAccount acc: customers) {
# if (accountNumber == acc.checkAccountNumber())
#     return acc;
# }
# throw
# new
# IncorrectAccountNumberException("No matching account found.");
# }
#
