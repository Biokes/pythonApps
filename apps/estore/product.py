from apps.estore import productCategory


class Product:
    product_id = ''
    product_name = ''
    product_price = 0.0
    product_desc = ''
    product_type = productCategory.ProductCategory

    def __init__(self,product_type, product_name, product_id, product_price, product_desc):
        self.product_type = product_type
        self.product_desc = product_desc
        self.product_name = product_name
        self.product_price = product_price
        self.product_id = product_id
        



