import pandas as pd
import numpy as np
import sqlalchemy as sqla
import ssl

from sqlalchemy import create_engine


ssl._create_default_https_context = ssl._create_unverified_context

#CSV, Excel, HTML, SQL

#CSV
df = pd.read_csv('pythonprojects\Intro_to_pandas\example.csv')

df.to_csv('My_Output', index = False)

pd.read_csv('My_Output')

#Excel
pd.read_excel('pythonprojects\Intro_to_pandas\Excel_Sample.xlsx', sheet_name='Sheet1')

df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

#HTML
df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

print(df[0].head())

#SQL

engine = create_engine('sqlite:///:memory:')

df[0].to_sql('my_table', engine)


sql_df = pd.read_sql('my_table',con=engine)

print(sql_df)