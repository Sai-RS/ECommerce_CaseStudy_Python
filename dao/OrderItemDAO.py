from util.DBConnUtil import DBConnection


class OrderItemDAO(DBConnection):

    def insertOrderItems(self, orderId, cartItems):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()

            for item in cartItems:
                data = (orderId, item[0], item[3])
                insert_query = "insert into order_items (order_id,product_id,quantity) values (%s,%s,%s)"

                cursor.execute(insert_query, data)

            connection.commit()
            connection.close()
        except Exception as e:
            print("In Order Item DAO - Insert Items", str(e))
