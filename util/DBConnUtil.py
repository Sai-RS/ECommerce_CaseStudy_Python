from mysql.connector import connect
from util.DBPropertyUtil import PropertyUtil

class DBConnection:
    def getConnection(self):
        try:
            data = PropertyUtil().getConnectionString()
            connection = connect(**data)
            return connection
        except Exception as e:
            print("Sorry! Couldn't connect to the database")
            return None
