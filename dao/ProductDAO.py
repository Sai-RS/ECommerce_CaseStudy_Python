from util.DBConnUtil import DBConnection
from exception.ProductNotFoundException import ProductNotFoundException

class ProductDAO(DBConnection):
    def createProduct(self,data):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            insert_query = "INSERT INTO products (name, price, description, stockQuantity) VALUES (%s, %s, %s, %s);"

            cursor.execute(insert_query, data)

            id = cursor.lastrowid

            connection.commit()
            connection.close()

            return id

        except Exception as e:
            print("In Product DAO - Create", str(e))
            return -1

    def deleteProduct(self, productId):
        try:
            connection = self.getConnection()
            data = (productId,)

            cursor = connection.cursor()
            delete_query = "delete from products where product_id = %s;"

            cursor.execute(delete_query, data)

            if cursor.rowcount == 0:
                raise ProductNotFoundException(productId)
            else:
                print("Product deleted successfully!")

            connection.commit()
            connection.close()

        except ProductNotFoundException as e:
            print(e)

        except Exception as e:
            print("In Product DAO - Delete", str(e))

    def getAllProducts(self):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            select_query = "select * from products"
            cursor.execute(select_query)

            rows = cursor.fetchall()
            return rows

        except Exception as e:
            print("In Product DAO - Retrieve", str(e))
            return None

    def updateProductQuantity(self, productId, quantity):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            data = (quantity, productId)
            update_query = "update Products set stockQuantity = stockQuantity - %s where product_id = %s"

            cursor.execute(update_query, data)
            connection.commit()
            connection.close()

        except Exception as e:
            print("In Product DAO - Update Quantity", str(e))
            return None

    def checkProductId(self, productId):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            select_query = "select * from products where product_id = %s"
            cursor.execute(select_query, (productId,))

            rows = cursor.fetchall()

            connection.commit()
            connection.close()

            if len(rows) == 0:
                raise ProductNotFoundException(productId)

        except ProductNotFoundException as e:
            print(e)

        except Exception as e:
            print("In Product DAO - Check Product Id", str(e))
