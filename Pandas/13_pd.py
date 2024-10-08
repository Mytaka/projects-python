import numpy as np
import pandas as pd

dict_array = {'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'], 
              'name': [53, 37, 11, 18, 7], 
              'наличие авто': [True, True, False, True, False]}

df = pd.DataFrame(dict_array, 
               index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4']
               )

df['name'].unique()  # возвращает уникальные значения серии или индексов
df['name'].nunique() # возвращает количество уникальных значений 
df.value_counts()    # возвращает мультииндексную серию с количевствои повторяющихся строк
df.value_counts(['name','age'], dropna=False) 
df.value_counts(normalize=True) # возвращает мультииндексную серию с пропорциями повторяющихся строк

df.sort_values('age')     # сортируют данные
df.sort_values(['age','name' ], na_position='first') # пропуски будут отображаться сверху, а обычно снизу