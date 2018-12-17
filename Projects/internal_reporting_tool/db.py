#!/usr/bin/env python3
import psycopg2


class DB():
    """ This DB class provides an interface between database and classes. """

    # BD, user and password
    USER = "app_user"
    PASS = "4pp_U$3R"
    BASE = 'news'

    def execute_query(self, query):
        """
        This execute_query method is responsible for creates a connection
        with database and executes a query

        It recives as paramiter:
            The query to be executed
        It returns:
            The result of the query
        """

        try:
            connection = psycopg2.connect(
                database=self.BASE,
                user=self.USER,
                password=self.PASS
            )
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except psycopg2.Error as err:
            print("DB error: {}".format(err))
        finally:
            connection.close()
