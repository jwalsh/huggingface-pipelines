#!/usr/bin/env python3
import pg8000 as pg

def db_conn():
    conn = pg.Connection(host='localhost', 
                         database='dev_database', 
                         user='postgres', 
                         password='yourPassword!')
    return conn

# Now you have a connection, query your data with a cursor

conn = db_conn()
cur = conn.cursor()
cur.execute('SELECT * FROM tab1')
data = cur.fetchall()

# Now 'data' contains your data, or use the new way with conn.run

if __name__ == '__main__':
    print('Grabbing data from tab1...')

    for row in conn.run('SELECT * FROM tab1'):
        print(row)

    conn.close()