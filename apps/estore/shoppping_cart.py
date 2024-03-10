from apps.apps import Items


class Cart:

    def __init__(self):
        self.cart = []

    def add_items_to_cart(self, item: Items):
        self.cart.append(item)

    def remove_items_from_cart(self, item: Items):
        self.cart.remove(item)
