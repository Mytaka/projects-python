import numpy as pn
import pandas as pd
import sqlite3 as sq

def create_table(db='Trifles/avito_data.db', path='Trifles/table.csv', name='avito'):
    con = sq.connect(db)

    df = pd.read_csv(path)
    df.to_sql(name, con, if_exists='replace', index=False)
    con.close()

create_table()   # создание таблицы
sql_request = '''SELECT * FROM avito'''   # SQL-запрос

# ---------------------------------------------------------------------------------------

with sq.connect('Trifles/avito_data.db') as con:
    df_sql = pd.read_sql(sql_request, con,
                         index_col='date2',            # столбец который будет исполнять роль индексов
                         index_col=['date1','date2'],  # мульти индекс
                         parse_dates=['E350']          # заменяет формат на datetime64
                         ) 

with sq.connect('Trifles/avito_data.db') as con:
    df_sql.to_sql('avito_0', con,
                 if_exists='fail',          # вернет ошибку при повторной записи 
                 if_exists='replace',       # перезапишет данные при повторной записи
                 if_exists='append',        # добавит данные при повторной записи
                 index=True,                # сохраняються ли индексы 
                 index_label='index_row'    # задает заголовок индексам
                  )

with sq.connect('Trifles/avito_data.db') as con:
    df_sql_read = pd.read_sql('''SELECT * FROM avito_0''', con)
print(df_sql_read)

