class Order_Item:
    def __init__(self):
        order_item_id = 0
        order_id = 0
        product_id = 0
        quantity = 0

    def setOrderItemId(self,order_item_id):
        self.order_item_id = order_item_id

    def setOrderId(self,order_id):
        self.order_id = order_id

    def setProductId(self,product_id):
        self.product_id = product_id

    def setQuantity(self,quantity):
        selg.quantity = quantity

    def getOrderItemId(self):
        return self.order_item_id

    def getOrderId(self):
        return self.order_id

    def getProductId(self):
        return self.product_id

    def getQuantity(self):
        return self.quantity