import numpy as np
import pandas as pd

df_1 = pd.DataFrame({'col_1': [5, 6, np.nan, 3, 7], 
                     'col_2': [27, 6, 7, 40, 70], 
                     'col_3': [1, 45, 6, 62, 7]}, 
                     index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

df_2= pd.DataFrame({'col_1': [5, 6, 7, np.nan, 3], 
                    'col_2': [27, 6, 7, 4, 7], 
                    'col_3': [1, 45, 6, 62, 7]}, 
                    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

series = pd.Series( [5, 6, np.nan, 1, 7], 
                   index=['row_10', 'col_2', 'row 3', 'row 4', 'row_5'])

# !!! все орифметически операции с np.nan вернут np.nan !!!
series + 5
series + np.nan
series + [1, 2, 3, 4, 5]         # нулевой с нулевым, первый с первым ...
series + df_1['col_1']           # сложение элементов с одинаковым индексом
df_1 + [1, 2, 3]                 # нулевой элемент списка добавляеться ко всем элементам первого столбца
df_3 = df_1.head(3)              # df_3 состоит с трех строк df_1
df_4 = df_1[['col_1', 'col_2']]  # df_4 состоит с двух столбцов df_1
df_4 + df_3                      # сложение элементов с одинаковым индексом

# add() - операция сложения 
# sub() - операция вычетания 
# div() - операция деления 
# mul() - операция умножения 
# pow() - операция возведение в степень 
# mod()- операция вычисления остатка от деления
df_1.add(100)
df_1.add([10,20,30]) # вдоль первой оси
df_1.add(df_2)
df_1.add([1,2,3,4,5], axis=0) # вдоль нулевой оси
df_1.add(series, axis=0)      # добавит серию к каждому столбцу
a = df_3.add(df_4, fill_value=10) # заменяет после сложения все элементы np.nan


print(a)

