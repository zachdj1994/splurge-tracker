import mysql.connector

class ChoresTable():
    connection = None

    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='grapes',
            host='127.0.0.1',
            database='splurge'
        )

    def getConnection(self):
        return self.connection

    def __del__(self):
        self.connection.close()
