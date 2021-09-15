import psycopg2
import datacompy
import pandas as pd

#Table to be compared
table_name = 'table_name'
#It could be the primary key for example
column_name = 'column_name'

#Postgres Connection
postgres = psycopg2.connect(
    host='host',
    database='database',
    user='user',
    password='password',
    port=5432
)

#Redshift Connection
redshift = psycopg2.connect(
    host='host',
    database='database',
    user='user',
    password='password',
    port=5439
)

#Loading Pandas Dataframes
df_postgres = pd.read_sql('SELECT * FROM ' + table_name, postgres)
df_redshift = pd.read_sql('SELECT * FROM ' + table_name, redshift)

#Comparing with Datacompy
compare = datacompy.Compare(
    df_postgres, 
    df_redshift,
    join_columns=column_name
)

#Showing Results
print(compare.report())