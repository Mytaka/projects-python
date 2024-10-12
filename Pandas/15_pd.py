import numpy as np
import pandas as pd

dct = { f'col_{i}': [i*1, 1*2, 1*3, 1*4, i*5] if i != 3 else [i, i, i, i, i] for i in range(5)}

df = pd.DataFrame(dct)

# Функции агрегации: 
# • min() 
# • max() 
# • mean() 
# • sum() 
# • std() 
# • count() 
# • first() 
# • last()
# ...

df.min()
df['col_1'].mean()

a = df.agg(np.min, axis=1)           # возвращает табл. с сделаной функцией
b = df.agg([np.min, np.max,np.mean]) # возвращает табл. с сделаными функциями

df.agg({'col_1': [np.min, np.sum],   # возвращает табл. с сделаными функциями
        'col_3': 'mean'})

df.agg(min_col_1=('col_1', 'min'), max_col_2=('col_2', np.max))

print(a,b)
