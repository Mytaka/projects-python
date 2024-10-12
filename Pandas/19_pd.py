import numpy as np
import pandas as pd

# df = pd.read_csv('file.csv', parse_dates=['date']) # при импрорте указываем на дату

df = pd.DataFrame({'id' : range(10000,10020),
                   'date' : pd.date_range('2023', periods=20, freq='D')})  # можно указать и W, M, Y, 

# pd.date_range('2023-03-10', '2023-05-30', Freq='M')             # указано начало и конец
# pd.date_range('2023-03-10', '2023-05-30', periods=10, Freq='M') # будет 10 дат с одинаковым интервалом

# df = df.astype({'date': ['datetime64[as]']})         # парсинг в дату
# df = pd.to_datetime('2023-02-12', format='%Y-%M-%D') # Y - год в формате 4 цифр, y - год в формате 2 цифр
# df = pd.to_datetime(df['date'])

# df['day_name'] = df['date'].dt.day_name() # .dt (аксцесор)- поэлементно .day_name() - вызов дня
# df['day'] = df['date'].dt.day
# df['month'] = df['date'].dt.month
# df['weekday'] = df['date'].dt.weekday   # день недели но в цифровом формате

df.loc[ df['date'] == pd.to_datetime('03-08-2016', format='%d-%m-%Y')] #перед тем, как проверять наличие даты, нужно поставить правильный формат

df.loc[1, 'date'].weekday

print(df)