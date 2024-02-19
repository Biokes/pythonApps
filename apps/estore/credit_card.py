from apps.estore.cardTypes import CardType


class CreditCard:

    def __init__(self, cvv: str, card_expirationDate: str, creditCardNumber: str, card_type: CardType, name_on_card: str):
        self.name_on_card = name_on_card
        if len(cvv) in 3:
            self.cvv = int(cvv)
        else:
            raise ValueError("invalid cvv provided.")
        if creditCardNumber.isnumeric() and len(creditCardNumber) in (13,14,15,16):
            self.creditCardNumber = creditCardNumber
        else:
            raise ValueError("invalid cardNumber")
        self.card_expirationDate = card_expirationDate
        self.card_type = card_type