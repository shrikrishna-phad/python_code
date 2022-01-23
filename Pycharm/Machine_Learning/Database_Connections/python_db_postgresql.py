# connection with postgresql

"""
pip install psycopg2
"""
import psycopg2

con = psycopg2.connect(database="python_connection",
                       user="root",
                       password="root")

print(con)