import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection = f'postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}'
engine = create_engine(connection)

with engine.connect() as conn:
    # 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
    with open('sql/drop.sql', 'r') as file:
        sql_script = file.read() 
        conn.execute(text(sql_script))  
    with open('sql/create.sql', 'r') as file:
        sql_script = file.read() 
        conn.execute(text(sql_script))  
    # 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
    with open('sql/insert.sql', 'r') as file:
        insert_script = file.read() 
        conn.execute(text(insert_script))
# 4) Use pandas to print one of the tables as dataframes using read_sql function
df = pd.read_sql('SELECT * FROM authors;', engine)
print(df)