class Address:

    def __init__(self, house_number: str, street: str, city: str, state: str, country: str):
        self.state = state
        self.street = street
        self.house_number = house_number
        self.country = country
        self.city = city

    def __str__(self):
        return f"{self.house_number}, {self.street}, {self.city} , {self.state}, {self.country}"
