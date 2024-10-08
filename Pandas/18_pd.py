import numpy as np
import pandas as pd

df_date = pd.DataFrame({'col_1': [0, 1, 2, 3, 4], 
                        'col_2': [90, 91, 92, 93, 94]})

df = df_date.rolling(3,             # скользящее окно
                     min_periods=1, # вставлять np.nan в строки, которые меньше аргумента
                     step=2,        # шаг
                     ) 
for window in df:  # можно перебрать окна
    print(window)

df_date.rolling(2).agg({'col_1': ['sum', 'mean', 'max', 'min'], 'col_2': 'mean'})  # можно использовать агригацию

print(df.sum())

# ---------------------------------------------------------------------------------
# Задача: усть список прибыли за 100 дней и просят посчитать сумы за каждые недели

np.random.seed(42)
df = pd.DataFrame({'sales': np.random.randint(0, 50, 100)}, 
                  index=pd.date_range('2023', periods=100))

df_rolling = df.rolling(7, min_periods=1).agg([np.sum, np.mean, np.max, np.min])
df_rolling.reset_index(inplace=True)
df_rolling['weekday'] = df_rolling['index'].dt.dayofweek
df_1 = df_rolling.loc[ df_rolling['weekday'] == 6 ]

print(df_rolling)

# Проверка

res = df['sales'][:'2023-04-09'].sum() == df_rolling.loc[ df_rolling['weekday'] == 6][('sales', 'sum')].sum()

print(res)

