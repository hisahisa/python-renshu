from contextlib import contextmanager
import mysql.connector


@contextmanager
def my_sql_conn(path):
    try:
        conn = mysql.connector.connect(
            user='root',
            passwd='',
            host='localhost',
            db='jawikipedia')
        # コネクションオブジェクトをコンテキストに渡す
        yield conn
    finally:
        if 'conn' in locals():
            conn.close()

# コネクションオブジェクトを as で受け取る
with my_sql_conn('db.sqlite3') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM page')
    for row in cursor:
        print(row)

