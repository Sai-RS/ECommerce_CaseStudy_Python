class Customer:
    def __init__(self):
        customerId = 0
        name = ''
        email = ''
        password = ''

    def setCustomerId(self,customerId):
        self.customerId = customerId

    def setName(self,name):
        self.name = name

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password

    def getCustomerId(self):
        return self.customerId

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password