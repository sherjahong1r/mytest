# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 04:53:50 2026

@author: Owner
"""

# pip install psycopg2-binary

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="example_db",
    user="postgres",
    password="jahongir"
)

# Jadvallar ro'yxati chiqarildi

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

cur.execute("""
SELECT table_name

FROM information_schema.tables
WHERE table_schema = 'public'
""")


print("\n\nJadvallar ro'yxatini ko'rish\nYani example_db dagi mavjud jadvallar\n")


tables = cur.fetchall()

for t in tables:
    print(t[0])

print("\n\nJadval malumotlarini chiqarish\n")

cur.execute("SELECT * FROM contacts_two")
rows = cur.fetchall()

for row in rows:
    print(row)
    
print("\nJadval ko'rinishida tartibli chiqarish\nFaqat contacts_two jadvaliniki\n")
    
import pandas as pd

df = pd.read_sql("SELECT * FROM contacts_two", conn)
print(df)

print("\n\nBu contacts_db yani ikkinchi db\n")

df_tables = pd.read_sql("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
""", conn)

print(f"\n{df_tables}\n")

print("\n")

df_dbs = pd.read_sql(
    "SELECT datname FROM pg_database WHERE datistemplate = false;",
    conn
)
print(f"\nMavjud db lar ro'yxati\n{df_dbs}\n")




