import psycopg2


class database(object):
    """
    Create the postgres database connection and return the connection object
    """

    def connection(db, user, host):
        connection_parameters = {
            'dbname': db,
            'user': user,
            'host': host
        }
        try:
            return psycopg2.connect(**connection_parameters)
        except BaseException:
            print("I am unable to connect to the database")
            conn.close()

    def query(connection, query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as error:
            message = "Error! unable to run query: " + query
            print(message)
            print(error)
        finally:
            connection.close()
