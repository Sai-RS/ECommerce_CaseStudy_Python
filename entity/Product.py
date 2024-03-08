class Product:
    def __init__(self):
        productId = 0
        name = ""
        price = 0
        description = ""
        stockQuantity = 0

    def setProductId(self,productId):
        self.productId = productId

    def setName(self,name):
        self.name = name

    def setPrice(self,price):
        self.price = price

    def setDescription(self,description):
        self.description = description

    def setStockQuantity(self,stockQuantity):
        self.stockQuantity = stockQuantity

    def getProductId(self):
        return self.productId

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def getStockQuantity(self):
        return self.stockQuantity