# CONNECTION WITH SSMS
"""
pip install pyodbc
"""

import pyodbc

con = pyodbc.connect("Driver={SQL Server};"
                     "Server=LAPTOP-AVKK09QV;"
                     "Database=python_connection;"
                     "Trusted_Connection=yes")

print(con)