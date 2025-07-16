import pandas as pd
from sqlalchemy import create_engine

# Step 1: Read the Excel file
df = pd.read_excel('/Users/rahulpokhrel/Desktop/excel/ETL/jobseek.xlsx')
# Step 2: Create a connection engine to PostgreSQL
engine = create_engine('postgresql://postgres:root@localhost:5432/postgres')

# Step 3: Write data to PostgreSQL
df.to_sql('jobseek', engine, if_exists='replace', index=False)


print("Data imported successfully!")
