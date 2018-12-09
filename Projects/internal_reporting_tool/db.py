import psycopg2


class DB():

    USER = "app_user"
    PASS = "4pp_U$3R"

    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query):
        connection = None
        try:
            connection = psycopg2.connect(database = self.db_name, user = self.USER, password = self.PASS)
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except psycopg2.Error as err:
            print("DB error: {}".format(err))
        finally:
            connection.close()
