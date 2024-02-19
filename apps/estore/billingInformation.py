from apps.estore.credit_card import CreditCard


class Billing_info:

    def __init__(self, receiver_no: str, receiver_name: str, delivery_address: str, card: CreditCard):
        self.receiver_no = receiver_no
        self.receiver_name = receiver_name
        self.delivery_address = delivery_address
        self.card = card
