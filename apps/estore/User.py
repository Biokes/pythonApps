from apps.apps.estore.address import Address


class User:

    def __init__(self, name: str, age: int, address: Address, email: str, password: str):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.password = password
