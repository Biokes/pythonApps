from apps.codedApps.estore.address import Address
from apps.codedApps.estore.cardTypes import CardType
from apps.codedApps.estore.credit_card import CreditCard
from apps.codedApps.estore.customer import Customer


class StoreTest:

    def test_customerAddBillingInfo_BillingInfoIsAdded(self):
        home_address: Address = Address("12", "Customer street", "meiran", "Lag", "Naija")
        customer: Customer = Customer("biokes", 17, home_address, "Email@email.com", "password")
        delivery_address: Address = Address("1", "receiver Street", "sabo", "lag", "naija")
        card: CreditCard = CreditCard("name ", "123", "12/27", "1234098765432", CardType.MASTERCARD, )
        customer.add_billling_info("receivers Name", "90908978", delivery_address, card)
        assert customer.get_number_of_billing_info() == 1
