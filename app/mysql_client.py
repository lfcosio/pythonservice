import mysql.connector


class MysqlClient:

    database = "quantaco_db"
    def __init__(self, host, user_name, password):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user_name,
            password=password
        )

    def create_db(self):
        if self.__database_exists():
            return
        with  self.mydb.cursor() as my_cursor:
            my_cursor.execute(f"CREATE DATABASE {self.database}")
        return

    def __database_exists(self):
        with  self.mydb.cursor() as my_cursor:

            my_cursor.execute("SHOW DATABASES")

            if self.database in my_cursor:
                return True
            return False


    def query_db(self, query):



