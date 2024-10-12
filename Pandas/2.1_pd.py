import pandas as pd
import numpy as np

pd_list = pd.Series([2,5,6.2,5,10],
                    index = ['row_1','row_2','row_3','row_4','row_5'], # меняет индексы
                    dtype='string', 
                    name = 'First')
print(pd_list)

# ---------------------------------------------------------------------------------------

# dict = {'row_1': 2,
#         'row_2': 3,
#         'row_3': 4}

# pd_list = pd.Series(dict,
#                     index = ['row_1','row_2','row_100'], # ищет значения за ключем
#                     dtype = int,
#                     name = "First")
                    
# print(pd_list) 

# ---------------------------------------------------------------------------------------

# np.random.seed(42)
# arr = np.random.randint(5,20, size=5)
# series = pd.Series(arr,
#                    copy=False) # используеться одна и та же ячейка памяти
#                                # copy=True - создаеться новая ячейка памяти

# print(series)

# # ---------------------------------------------------------------------------------------

# series1 = pd.Series([2,5,6.2,5,10])
# series2 = pd.Series(series1,
#                     index = [0,3,1])
# print(series2)


