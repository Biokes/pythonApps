from apps.apps.estore.address import Address
from apps.apps.estore.customer import Customer


class EStoreTest:

    def test_customerAddBillingInfo_BillingInfoIsAdded(self):
        home_address: Address = Address("12", "Street street", "meiran", "Lag", "Naija", )
        customer: Customer = Customer("biokes", "Email@email.com", home_address, "password")
