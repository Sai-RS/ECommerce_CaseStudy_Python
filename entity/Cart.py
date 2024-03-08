class Cart:
    def __init__(self):
        cardId = 0
        customerId = 0
        productId = 0
        Quantity = 0

    def setCartId(self,cartId):
        self.cartId = cartId

    def setCustomerId(self,customerId):
        self.customerId = customerId

    def setProductId(self,productId):
        self.productId = productId

    def setQuantity(self,quantity):
        self.quantity = quantity

    def getCartId(self):
        return self.cartId

    def getCustomerId(self):
        return self.customerId

    def getProductId(self):
        return self.productId

    def getQuantity(self):
        return self.quantity