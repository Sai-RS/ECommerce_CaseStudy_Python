class OrderNotFoundException(Exception):
    def __init__(self,productId):
        super().__init__(f'Order Id {productId} is not found in the database')