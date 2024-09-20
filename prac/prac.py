import numpy as pn
import pandas as pd
import sqlite3 as sq

def create_table(db='Trifles/avito_data.db', path='Trifles/avito_data.csv', name='avito'):
    con = sq.connect(db)

    df = pd.read_csv(path)
    df.to_sql(name, con, if_exists='replace', index=False)
    con.close()

create_table()  # создание таблицы

sql_request = '''SELECT * FROM avito'''  # SQL-запрос

df = pd.read_csv('D:/projects/projects-python/Trifles/avito_data.csv')
print(df)
