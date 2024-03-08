class Order:
    def __init__(self):
        order_id = 0
        customer_id = 0
        order_date = ''
        total_price = 0
        street = ''
        city = ''
        state = ''
        pincode = 0

    def setOrderId(self,order_id):
        self.order_id = order_id

    def setCustomerId(self,customer_id):
        self.customer_id = customer_id

    def setOrdeDate(self,order_date):
        self.order_date = order_date

    def setTotalPrice(self,total_price):
        self.total_price = total_price

    def setStreet(self,street):
        self.street = street

    def setCity(self,city):
        self.city = city

    def setState(self,state):
        self.state = state

    def setPincode(self,pincode):
        self.pincode = pincode

    def getOrderId(self):
        return self.order_id

    def getCustomerId(self):
        return self.customer_id

    def getTotalPrice(self):
        return self.total_price

    def getOrderDate(self):
        return self.order_date

    def getStreet(self):
        return self.street

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getPincode(self):
        return self.pincode