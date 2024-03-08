from util.DBConnUtil import DBConnection

class CustomerDAO(DBConnection):
    def registerCustomer(self):
        try:
            connection = self.getConnection()

            name = input("Enter your Name: ")
            email = input("Enter your Email: ")
            password = input("Enter your Password: ")

            data = (name, email, password)
            cursor = connection.cursor()
            insert_query = "INSERT INTO customer (name, email, password) VALUES (%s, %s, %s);"

            cursor.execute(insert_query, data)
            customerId = cursor.lastrowid

            connection.commit()
            connection.close()

            return customerId

        except Exception as e:
            print("In Customer DAO", str(e))
            return -1

    def checkCustomerId(self,customerId):
        try:
            connection = self.getConnection()

            cursor = connection.cursor()
            select_query = "select * from customer where customer_id = %s"
            cursor.execute(select_query, (customerId,))

            rows = cursor.fetchone()

            connection.commit()
            connection.close()
            return rows

        except Exception as e:
            print("In Customer DAO", str(e))
            return None
