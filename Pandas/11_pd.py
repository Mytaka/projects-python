import numpy as np
import pandas as pd


# df = pd.DataFrame({'col_1': [5, 6, np.nan, 3, 7], 
#                    'col_2': [27, 6, 7, 40, 70], 
#                    'col_3': [1, 45, 6, 62, 7]}, 
#                    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

# df.drop(
#         'row_2',         # удаляет ось с этим элементом 'labels='
#         axis=1,          # какую усь будем удалять
#         index='row_3'    # имена, которые нужно удалить
#         columns='col_3'  # имена, которые нужно удалить
#         ) 

# -------------------------------------------------------------------------

category_list = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame({'col_1': [ i for i in range(1000)], 
                'col_2': [ float(i) for i in range(1000)], 
                'col_3': [category_list[i%5] for i in range(1000)], 
                'col_4': [ *pd.date_range(start='01-01-2000', periods=1000).strftime("%m-%d-%Y") ]}, 
                index=[ f'row_{i}' for i in range(1000)])

df.memory_usage() # возвращает сирию, где показано, сколько байтов выделяеться на каждый столбец

# new_df = df.astype({'col_1': np.int8})       # astype - меняет тип данных
# new_df = df.astype({'col_3': 'category'})
# new_df = df.astype({'col_4': 'datetime64[ns]'})

new_df = df.astype({'col_1': np.int16,
                    'col_2': np.float16,
                    'col_3': 'category',
                    'col_4': 'datetime64[ns]'})
new_df.reset_index(drop=True, inplace=True)     # убирает индексы

print(new_df.memory_usage())

