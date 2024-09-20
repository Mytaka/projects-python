import numpy as np
import pandas as pd

np.random.seed(42)

df = pd.DataFrame(np.random.randint(25,size=(5,5)),
                #   index=['row_1','row_2','row_3','row_4','row_5'],
                  columns=['col_1','col_2','col_3','col_4','col_5']
                  )
                  
res = df.set_index('col_1') # из столбца делает индексы
print(res)