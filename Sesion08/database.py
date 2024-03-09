import mysql.connector
import os

class MySQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.pw = password
        self.db = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            if (self.connection == None):
                self.connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.pw,
                    database = self.db
                )
                os.system("color a2")
                print("Wow, me conecte sastisfactoriamente")
        except mysql.connector.Error as error:
            print("Error mientras se estaba conectando {}".format(error))

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close
                self.connection = None
        except mysql.connector.Error as error:
            print("Error")

    def execute_querry(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")

db = MySQLDB("localhost", "root", "123", "test")
print("Conectado")

db.connect()
#db.disconnect()
#categorias = db.execute_querry("select * from categorias")