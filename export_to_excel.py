import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",       # or your actual DB name
    user="postgres",
    password="root"   # replace with your actual password
)

# SQL query
query = "SELECT * FROM employee_data;"  # or your actual table

# Read data into pandas DataFrame
df = pd.read_sql(query, conn)

# Save to Excel file
df.to_excel("employee_data.xlsx", index=False)

print("✅ Exported to employee_data.xlsx")
