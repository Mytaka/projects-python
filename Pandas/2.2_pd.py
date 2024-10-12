import numpy as np
import pandas as pd

dict = {'col1': [5, 6, 6, 3, 7],   # количество элементов должно быть как в матрице
        'col2': [27, 6, 7, 4, 7],
        'col3': [1, 45, 6, 62, 7],
        'col4': [65, 6, 7, 82, 7],
        'col5': [8, 3, 2, 5, 11]}

df = pd.DataFrame(dict,
                  index=['row_1','row_2','row_3','row_4','row_5'],
                  columns=['col4','col1','5'],
                  dtype=int,
                  copy=False) # используеться одна и та же ячейка памяти
                              # copy=True - создаеться новая ячейка памяти

print(df)

