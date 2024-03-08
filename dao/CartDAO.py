from util.DBConnUtil import DBConnection
from dao.ProductDAO import ProductDAO
from dao.CustomerDAO import CustomerDAO
from exception.ProductNotFoundException import ProductNotFoundException

class CartDAO(DBConnection):

    def addToCart(self,customerId,productId,quantity):
        try:
            connection = self.getConnection()

            products = ProductDAO().getAllProducts()

            flag = "False"
            for p in products:
                if p[0] == productId:
                    if quantity > p[4]:
                        print("\nSorry! Quantity exceeds the Product Quantity")
                        flag = "Exceeds"
                    else:
                        flag = "True"
                    break

            if flag == "True":
                cursor = connection.cursor()
                ProductDAO().updateProductQuantity(productId, quantity)

                row = CartDAO().checkProductInCart(productId, customerId)

                if row is None:
                    data = (customerId, productId, quantity)
                    insert_query = "insert into cart (customer_id,product_id,quantity) values (%s,%s,%s)"

                    cursor.execute(insert_query, data)
                else:
                    data = (quantity, customerId, productId)
                    update_query = ("update cart set quantity = quantity + %s where customer_id = %s and "
                                    "product_id = %s")

                    cursor.execute(update_query, data)

                print("Product Added to your cart!!!")

                connection.commit()
                connection.close()

            elif flag == "False":
                raise ProductNotFoundException(productId)

        except ProductNotFoundException as e:
            print(e)

        except Exception as e:
            print("In Cart DAO", str(e))

    def checkProductInCart(self, productId, customerId):
        try:
            connection = self.getConnection()
            data = (productId, customerId)

            cursor = connection.cursor()
            select_query = "select * from cart where product_id = %s and customer_id = %s"

            cursor.execute(select_query, data)
            row = cursor.fetchone()

            connection.commit()
            connection.close()

            return row

        except Exception as e:
            print("In Cart DAO - Product Check", str(e))
            return None

    def getAllFromCart(self, customerId):
        try:
            connection = self.getConnection()
            data = (customerId,)

            cursor = connection.cursor()
            select_query = ("select cart.product_id,name,price,quantity from cart join products on cart.product_id = "
                            "products.product_id where customer_id = %s")
            cursor.execute(select_query, data)

            rows = cursor.fetchall()

            connection.commit()
            connection.close()

            return rows

        except Exception as e:
            print("In Cart DAO - Get Cart", str(e))
            return None

    def removeFromCart(self,customerId):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            delete_query = "delete from cart where customer_id = %s"
            cursor.execute(delete_query, (customerId,))

            connection.commit()
            connection.close()
        except Exception as e:
            print("In Cart DAO - Delete Cart", str(e))
            return None