class CustomerNotFoundException(Exception):
    def __init__(self,customerId):
        super().__init__(f'\n******  No Customer is found with the customer id {customerId}  ******')