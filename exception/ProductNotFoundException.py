class ProductNotFoundException(Exception):
    def __init__(self,productId):
        super().__init__('No products available with this product id')