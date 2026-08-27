# ============================================================
# SQL Constraints
# Activity: World Cities Database
# ============================================================

# ---- PART 1: Create the Table with Constraints ----
# SQL constraints are rules written inside CREATE TABLE.
# They control what data each column is allowed to store.
# If a row breaks a constraint, the insert is rejected.
# Constraints keep the database accurate and reliable.

import sqlite3
import pandas as pd

conn = sqlite3.connect('MYSQL/cities.db')

conn.execute("DROP TABLE IF EXISTS City;")

conn.execute("""
CREATE TABLE City (
    City_Id    INTEGER  PRIMARY KEY,
    City_Name  TEXT     NOT NULL UNIQUE,
    Country    TEXT     NOT NULL,
    Population INTEGER,
    Is_Capital TEXT     DEFAULT 'No'
);
""")
conn.commit()
print("Table created successfully!")

# ---- PART 2: INSERT — Adding Rows to the Table ----
# INSERT INTO adds one row at a time.
# Every NOT NULL column must receive a value.
# Columns with a DEFAULT can be left out — the default fills in.
# conn.commit() saves all inserts permanently.

conn.execute("INSERT INTO City VALUES (1, 'Tokyo',     'Japan',      13960000, 'Yes');")
conn.execute("INSERT INTO City VALUES (2, 'Nairobi',   'Kenya',       4397000, 'Yes');")
conn.execute("INSERT INTO City VALUES (3, 'Mumbai',    'India',      20667656, 'No');")
conn.execute("INSERT INTO City VALUES (4, 'Sao Paulo', 'Brazil',     12325232, 'No');")
conn.execute("INSERT INTO City VALUES (5, 'London',    'UK',          9541000, 'Yes');")
conn.execute("INSERT INTO City (City_Id, City_Name, Country) VALUES (6, 'Sydney', 'Australia');")
conn.commit()
print("Rows inserted successfully!")

cities = pd.read_sql("SELECT * FROM City;", conn)
print(cities)

# ---- PART 3: PRIMARY KEY in Action ----
# PRIMARY KEY uniquely identifies every row.
# No two rows can share the same City_Id.
# The column also cannot be NULL.
# Trying to insert a duplicate PRIMARY KEY raises an error.

# Add PART 3. Write a try / except block that attempts to insert City_Id 1 with a different city name. The PRIMARY KEY constraint will reject it with 'UNIQUE constraint failed'. Call conn.rollback() inside the except block and print a message explaining what happened.


print("\n--- Testing PRIMARY KEY ---")
try:
    conn.execute("INSERT INTO City VALUES (1, 'Cairo', 'Egypt', 21323000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Id 1 already belongs to Tokyo — PRIMARY KEY must be unique.")

# ---- PART 4: NOT NULL and UNIQUE in Action ----
# NOT NULL means the column cannot be left without a value.
# UNIQUE means no two rows can share the same value in that column.
# City_Name is both NOT NULL and UNIQUE — it must exist and must differ per row.

#Step 4:

# Add PART 4. Write two try / except blocks. The first attempts to insert a row with NULL as the Country value — NOT NULL will reject it. The second attempts to insert a row with City_Name 'Tokyo' — UNIQUE will reject it. Both need conn.rollback() in their except block.

print("\n--- Testing NOT NULL ---")
try:
    conn.execute("INSERT INTO City VALUES (7, 'Berlin', NULL, 3645000, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("Country is NOT NULL — every row must provide a country value.")


# Step 5:

# Add PART 5. Use pd.read_sql() with WHERE City_Name = 'Sydney' to select Sydney's row. Print it and observe that Is_Capital shows 'No' even though you never provided that value — the DEFAULT filled it in automatically.



print("\n--- Testing UNIQUE ---")
try:
    conn.execute("INSERT INTO City VALUES (8, 'Tokyo', 'Japan', 99999, 'No');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name is UNIQUE — 'Tokyo' is already in the table.")

# ---- PART 5: DEFAULT in Action ----
# DEFAULT sets an automatic value when no value is provided for a column.
# Sydney (row 6) was inserted without Is_Capital.
# The DEFAULT 'No' was applied automatically.


#Step 6:

# Add PART 6. SELECT City_Name, Country, and Population for all rows and print the full result — Sydney's Population will show NaN (NULL). Then write a query with WHERE Population IS NULL to find cities with missing population data. Write a second query with WHERE Population IS NOT NULL to find cities with data. Print both results. Add conn.close() at the very end.

print("\n--- DEFAULT value check for Sydney ---")
sydney = pd.read_sql("""SELECT City_Name, Country, Is_Capital
    FROM City
    WHERE City_Name == 'Sydney';""", conn)
print(sydney)
print("Is_Capital was not given — DEFAULT 'No' was used automatically.")

# ---- PART 6: NULL Values ----
# NULL means no value is stored — it is not zero and not an empty string.
# It is the complete absence of data.
# A column without NOT NULL can store NULL.
# Use IS NULL to find rows where data is missing.
# Use IS NOT NULL to find rows where data was provided.

print("\n--- NULL in the Population column ---")
all_cities = pd.read_sql("""SELECT City_Name, Country, Population
    FROM City;""", conn)
print(all_cities)

missing = pd.read_sql("""SELECT City_Name FROM City
    WHERE Population IS NULL;""", conn)
print("Cities with no population data:")
print(missing)

has_data = pd.read_sql("""SELECT City_Name, Population FROM City
    WHERE Population IS NOT NULL;""", conn)
print("Cities with population data:")
print(has_data)

conn.close()
