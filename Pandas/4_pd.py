import numpy as np
import pandas as pd

np.random.seed(42)

df = pd.DataFrame(np.random.randint(25,size=(5,5)),
                  columns=['col_1','col_2','col_3','col_4','col_5']
                  )
                  
res = df.set_index('col_1')           # из столбца делает индексы
df.set_index(['col_1','col_3'],
             append=True,             # стоит ли оставлять старый индекс
             inplace=True             # применяет сразу | inplace=False возвращает результат
             )      
print(df)

# ---------------------------------------------------------------------------------------

res = df['col_2']             # возвращает сирию
res = df[['col_2', 'col_1']]  # возвращает датафрейм
df[['col_1','col_2']] = 1     # замняет значения в слтолбцах на 1
df['NEW_col'] = 2             # создает новую столбец со значениями 2
del df['NEW_col']             # удалить столбец
res = df.col_1                # возвращает столбец
res = df[[False, False, True, True, False]]            # возвращает строки с совпадающими индексами и True
res = df[[False, False, True, True, False]] = 100
res = df[[False, False, True, True, False]][['col_1']] # возвращает строки с совпадающими индексами и True в столбце

print(res)


