from apps.apps.estore.address import Address
from apps.apps.estore.User import User


class Customer(User):

    def __init_subclass__(self, name: str, age: int, address: Address, password: str, number: str):
        super.__init__(name, age, address, password, number)
