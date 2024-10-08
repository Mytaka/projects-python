import numpy as np
import pandas as pd

# arr = [[1, 1, 2, 2], ['row_1', 'row_2', 'row_3', 'row_4']]     # пандас беред элемент первого уровня и сапоставляет с элементами второго уровня ...
# multi = pd.MultiIndex.from_arrays(arr, names=['level_0','level_1'])

# level_0= ['row_1', 'row_2']     # пандас беред элемент первого уровня и сапоставляет с каждым элементом второго уровня ...
# level_1= [1, 2]
# multi = pd.MultiIndex.from_product([level_0,level_1], names=['level_0','level_1']) 

# tuples = [(1, 'row_1'), (1, 'row_2'), (2, 'row_1'), (2, 'row_2')] 
# multi = pd.MultiIndex.from_tuples(tuples, names=['level_0','level_1'])
# print(multi)

# df = pd.DataFrame ([[4, 3, 2, 1], 
#                     [4, 3, 2, 1], 
#                     [4, 3, 2, 1], 
#                     [4, 3, 2, 1]], 
#                     index=multi,
#                     columns=multi
#                     )

# df.index
# df.columns

# df.index.nlevels   # возвращает число уровней индексов
# df.index.levshape  # возвращает картеж с длиной каждого уровня
# df.index.names     # возвращает имена уровней или меняет их
# df.index.names = ['new_level_0', 'new_level_1']
# df.index.levels    # элементы в мультииндексе
# df.index = multi   # меняет мультииндекс
# new_index = df.index.set_levels([[4, 5, 6], ['q', 'w', 'r', 't', 'p']]) # возвращает новый мультииндекс
# new_index = df.index.set_levels(['q', 'w', 'r', 't'], level=0)
# df.reset_index()   # возвращает новый датафрейм с мультииндексами
# df.reset_index(['level_0'], # нулевой уровень представлен в виде столбца
#                inplace=True)
# new_index = df.index.droplevel(            # возвращает индекс с удаленным нулевым элементом
#                                level=1     # возвращает индекс с удаленным первым элементом
#                                ['level_1'] # возвращает индекс с удаленным списком жлементов
#                                ) 

# df.index.set_names(['new_level_0', 'new_level_1'],  # меняет индексы
#                    level='1',     # поменять название конкретного уровня
#                    inplace=True)  # меняет исходный индекс*


