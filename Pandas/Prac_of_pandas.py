import numpy as np
import pandas as pd

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))

# ser = pd.Series(mydict)
# print(ser)

# -----------------------------------------------------------------------------------------

# mylist = list('abcedfghijklmnopqrstuvwxyz')
# myarr = np.arange(26)
# mydict = dict(zip(mylist, myarr))
# ser = pd.Series(mydict)
# df = ser.to_frame().reset_index()
# print(df)

# -----------------------------------------------------------------------------------------

# ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ser2 = pd.Series(np.arange(26))
# df = pd.DataFrame({'col_1': ser1,
#                    'col_2': ser2})
# print(df)

# -----------------------------------------------------------------------------------------

# ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'),
#                 name = 'alphabets')
# print(ser)

# -----------------------------------------------------------------------------------------

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# ser1 = ser1[~ser1.isin(ser2)] # ~ - инверсия булевых значений
# print(ser1)

# -----------------------------------------------------------------------------------------

# ser1 = pd.Series([1, 2, 3, 4, 5])
# ser2 = pd.Series([4, 5, 6, 7, 8])
# ser = pd.Series(np.union1d(ser1,ser2))
# print(~ser1.isin(np.intersect1d(ser1,ser2)), ~ser2.isin(np.intersect1d(ser1,ser2)))

# print()

# -----------------------------------------------------------------------------------------
# Рассчитай среднюю температуру для каждого месяца, построй изменение температуры по времени и 
# определи, в каком месяце была самая высокая и самая низкая температура.

df = pd.read_csv('Trifles/weather_data.csv')

df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month

temp = df.groupby('month').agg('temperature').mean()

print('min: ',temp.min())
print('min: ',temp.max())
