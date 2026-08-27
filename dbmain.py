import sqlite3
import pandas as pd

conn = sqlite3.connect("MYSQL/mydatabase.db")

tables = pd.read_sql("""
SELECT *
FROM sqlite_master
WHERE type='table';
""", conn)

print(tables)

conn.close()