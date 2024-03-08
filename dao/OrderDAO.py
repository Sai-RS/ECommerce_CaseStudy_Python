from util.DBConnUtil import DBConnection
from dao.CartDAO import CartDAO
from dao.OrderItemDAO import OrderItemDAO
import datetime

class OrderDAO(DBConnection):

    def placeOrder(self,data):
        try:
            connection = self.getConnection()

            customerId,street,city,state,pincode = data

            cartItems = CartDAO().getAllFromCart(customerId)
            total_price = 0

            # Printing Cart Items for reference

            print("\nYour Cart")
            print("*********\n")

            headers = ["Product Id","Name","Price","Quantity"]
            header_row = "|".join(f"{header:<27}" for header in headers)
            print(header_row)
            print("-" * len(header_row))

            # Print data rows
            for row in cartItems:
                data_row = "|".join(f"{str(item):<27}" for item in row)
                total_price+=row[2]*row[3]
                print(data_row)

            # Order Date
            order_date = datetime.date.today()

            # Insert Order
            cursor = connection.cursor()
            data = (customerId,order_date,total_price,street,city,state,pincode)
            insert_query = ("insert into orders (customer_id,order_date,total_price,street,city,state,pincode) values "
                            "(%s,%s,%s,%s,%s,%s,%s);")
            cursor.execute(insert_query, data)

            # Retrieving Order Id
            orderId = cursor.lastrowid
            connection.commit()
            connection.close()

            # Inserting Order items

            OrderItemDAO().insertOrderItems(orderId, cartItems)

            # Removing Cart Items after Ordering

            CartDAO().removeFromCart(customerId)
            return [orderId,total_price]

        except Exception as e:
            print("In Order DAO - Place Order", str(e))
            return -1

    def getOrdersByCustomer(self,customerId):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            select_query = "select order_id,order_date,total_price from orders where customer_id = %s"
            cursor.execute(select_query, (customerId,))

            rows = cursor.fetchall()
            connection.commit()
            connection.close()

            return rows

        except Exception as e:
            print("In Order DAO - Get Orders", str(e))
