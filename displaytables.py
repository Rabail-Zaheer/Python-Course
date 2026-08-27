import sqlite3
import pandas as pd

conn = sqlite3.connect("MYSQL/mydatabase.db")

Customer = pd.read_sql("""
SELECT * FROM Customer;
""", conn)

print(Customer)