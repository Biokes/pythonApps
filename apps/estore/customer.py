from apps.apps.estore.address import Address
from apps.apps.estore.User import User
from apps.apps.estore.credit_card import CreditCard


class Customer(User):

    def __init__(self, name: str, age: int, address: Address, password: str, number: str):
        super.__init__(name, age, address, password, number)

    def get_number_of_billing_info(self):
        pass

    def add_billling_info(self, recievers_name: str, receivers_number: str, delivery_address: Address,
                          card: CreditCard):
        pass
