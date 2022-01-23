import mysql.connector
def connect_to_mysql(fun):
    def inner(*args):
        conn = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='root',
                                       database='python_connection')
        cur = conn.cursor()
        fun(conn,cur, *args)
        conn.close()

    return inner

