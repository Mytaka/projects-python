import numpy as np
import pandas as pd

# list_index = list('qwert')

# index_data = pd.Index(list_index,
#                     #   dtype=np.float32,
#                       name = 'row')
# print(index_data)

# colum_data = pd.Index(['col_1','col_2','col_3'],
#                       name = 'cols')

# df = pd.DataFrame({'col_1': [5, 6, 6, 3, 7],  
#                    'col_2': [27, 6, 7, 4, 7],
#                    'col_3': [1, 45, 6, 62, 7]},
#                    index=index_data,
#                    columns=colum_data
#                    )
# print(df)

# ---------------------------------------------------------------------------------------

# df = pd.DataFrame( {f'c_{i}': np.arange(1000)*i for i in range(10)})
# print(df)

# index = df.index      # возвращает RangeIndex(start=0, stop=1000, step=1)
# columns = df.columns  # возвращает список с назаваниями столбцов
# df.columns = [[f'col_{i}' for i in range(10)]]
# columns = df.columns

# index.to_list()       # возвращает индексы в список
# columns.to_list()     # возвращает название столбцов в список

# index.to_numpy()      # возвращает индексы в масив numpy
# columns.to_numpy()    # возвращает название столбцов в numpy

# index.unique()        # возвращает уникальные индексы
# columns.unique()      # возвращает уникальные название столббцов

# index.nunique()       # возвращает количество уникальных индексов
# columns.nunique()     # возвращает количество уникальных названий столббцов

# index.is_unique()     # проверяет все ли значения уникальные
# columns.is_unique()   # проверяет все ли значения уникальные

# index.duplicated()    # возвращает список с булевыми переменными, False - если элемент встречаеться впервые, а True - уже встречался
# columns.duplicated()  # возвращает список с булевыми переменными, False - если элемент встречаеться впервые, а True - уже встречался

# index.name = 'Mytka'
# columns.name= 'Barri'
# index.name()          # возвращает имя индексов 
# columns.name()        # возвращает имя столбцов 

# df_lox = df.rename(columns = {'col_1': 'Barri', # возвращает DataFrame с переделаными названиями 
#                               'col_0' :  'lox'})

# df_lox = df.rename( #{'col_1': 'Barri', 
#                     # 'col_0' :  'lox'}, 
#                      str.upper,
#                      axis=1,
#                      inplace=True # применяет сразу | inplace=False возвращает результат
#                      )
# print(df_lox)

# ---------------------------------------------------------------------------------------

# index = pd.Index([3, np.nan, 4, np.nan,5])

# df = pd.DataFrame(np.arange(5), index=index)
# print(df)

# df.index.hasnans    # есть ли пропуски в индексах
# df.columns.hasnans  # есть ли пропуски в столбцах

# df.index.isna()     # возвращает масив в кторотом True = Nan
# df.columns.isna()   # возвращает масив в кторотом True = Nan

# df.index.dropna()   # возвращает индексы с удаленными пропусками 
# df.columns.dropna() # возвращает столбцы с удаленными пропусками


