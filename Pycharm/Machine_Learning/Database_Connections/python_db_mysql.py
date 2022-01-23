"""
BEFORE CONNECTING

pip install mysql-connector-python
"""

import mysql.connector

"""
# CONNECTION OBJECT

con = mysql.connector.connect(host='localhost',
                              user='root',
                              password='root')

# TO CHECK CONNECTION

print(con)
print(con.connection_id)


# Creating cursor object

cur = con.cursor()

# CREATE DATABASE
cur.execute("create database python_connection")

# NOW CONNECT WITH CREATED DATABASE
"""

con = mysql.connector.connect(host='localhost',
                              user='root',
                              password='root',
                              database='python_connection')
cur = con.cursor()

"""
cur.execute("create table employee (eid int,ename varchar(20),esal int)")

# INSERT ONE VALUE
var = "insert into employee values (101,'rahul','5000')"

cur.execute(var)

# COMMIT CHANGES

con.commit()


# INSERT MULTIPLE VALUES
var = "insert into employee values (%s,%s,%s)"
values = [
    (102,'amit',7000),
    (103,'sumit',10000),
    (104,'sandesh',11000)]

cur.executemany(var,values)
con.commit()


# FETCHING DATA

q = "select * from employee"
cur.execute(q)
data = cur.fetchall()
print(data)

for i in data:
    print(i)

# UPDATE TABLE

q = "update employee set eid=001 where eid = 101"
cur.execute(q)
con.commit()

# DELETE FROM TABLE

q = "delete from employee where eid = 1"
cur.execute(q)
con.commit()
"""
