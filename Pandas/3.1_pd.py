import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------------------

df_sep = pd.read_csv('Trifles/table.csv', 
                     sep=';',                          # выбираем будет раздедитель
                     index_col=['E350'],               # колонка вынесеная на перед
                     usecols=['E350','1997','Ford'],   # импортированые колонки
                     dtype = {'E350': 'category'},     # заменить тип данных в колонке
                     nrows=7,                          # импортируеться указаное количество строк
                                                    
                     parse_dates=['date1'],                   # заменяет формат на datetime64
                     parse_dates=[['date1','date2']],         # объеденяет колонки с датами (день, месяц тд.)
                     parse_dates={'date': ['date1','date2']}, # объеденяет колонки с датами, при этом давая им название
                     ) 
print(df_sep)

# ---------------------------------------------------------------------------------------

df = pd.read_csv('Trifles/table.csv', encoding='utf8', # кодировка
                 parse_dates=[['date1','date2']],
                 infer_datetime_format=True     # может ускорить парсинг 50\50
                 keep_date_col=True             # после парсинга колонки не удаляються ( не работает с infer_datetime_format)
                                                # Fale - удаляються
                 ) 
print(df)

# ---------------------------------------------------------------------------------------

df_sep = pd.read_csv('Trifles/table.csv',
                     sep=';',           
                     ) 
sep_Series = df_sep['E350'] # преобраование в Series
print(sep_Series)


