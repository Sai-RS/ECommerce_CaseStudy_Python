class PropertyUtil:
    host = "localhost"
    database = "ecommerce"
    username = "root"
    password = "Saibharathi@19"

    def getConnectionString(self):
        return {"host": PropertyUtil.host, "database": PropertyUtil.database, "username": PropertyUtil.username,
                "password": PropertyUtil.password}

# database = connect(host = "localhost", database = "ecommerce", username = "root", password = "Saibharathi@19")
# print(database)
