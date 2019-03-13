#!/usr/bin/env python

import psycopg2

def create_connection(db, user, host):
    connection_parameters = {
        'dbname': db,
        'user': user,
        'host': host
    }
    try:
        return psycopg2.connect(**connection_parameters)
    except:
        print("I am unable to connect to the database")
        conn.close()

def exec_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)

    return cursor.fetchall()

try:
    connection = create_connection('news', 'postgres', 'localhost')
    results = exec_query(connection, "select * from articles;")
    print(results)
except:
    print("unable to return query results")
finally:
    connection.close()
