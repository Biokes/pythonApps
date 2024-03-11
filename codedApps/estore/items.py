from apps.codedApps import Product


class Items:

    def __init__(self, product: Product, product_quantity: int):
        self.product = product
        self.product_quantity = product_quantity
