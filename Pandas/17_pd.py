import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['80', 'B1', 'B2', 'B3'], 
                    'C': ['CO', 'C1', 'C2', 'C3'], 
                    'D': ['D0', 'D1', 'D2', 'D3']}, 
                    index=[0, 1, 2, 3])
df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"], 
                    "B": ["84", "B5", "B6", "B7"], 
                    "C": ["C4", "C5", "C6", "C7"], 
                    "D": ["D4", "D5", "D6", "D7"]}, 
                    index=[1, 2, 3, 4])
df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"], 
                    "B": ["88", "89", "810", "B11"], 
                    "C": ["C8", "C9", "C10", "C11"], 
                    "D": ["D8", "D9", "D10", "D11"]},
                    index=[2, 3, 4, 5])
 
df=pd.concat([df1,df2,df3],     # объеденение датафреймов в виде большого столбца
          ignore_index=True,    # будет ли создаваться новая индексация?
          axis=1                # объеденить строки с одинаковыми индексами
          ) 
print(df)

# -------------------------------------------------------------------------

df_1 = pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21998, 455323, 455323, 21990, 455323,], 
                         'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product3','product3','product3','product6']})

df_2 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'], 
                    'price': [1000, 2000, 3000, 4000, 5000]})

# левая - df_1, правая - df_2
df=df_1.merge(df_2,             # объеденение по столбцам  с одинаковыми названиями
            how='left',       # только то, что есть в левой функции
            how='right',      # только то, что есть в правой функции
            how='inner',      # только то, что есть в обоих функциях. Умолчание
            how='outer',      # все элементы
            on='product',     # имя столбца по которому будет идти объеденениэ
               )
print(df)

# -------------------------------------------------------------------------

df_1= pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21990, 455323, 455323, 21990, 455323],
                        'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product_3','product_3','product_3','product_6'],
                        'color_prod': ['black', 'white', 'white', 'white', 'black', 'black', 'white', 'black','white']})

df_2 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5', 'product_1','product_2','product_3','product_4'],
                         'price': [1000, 2000, 3000, 4000, 5000, 1500, 2500, 3500, 4500],
                         'color_prod': ['black', 'black', 'black', 'black', 'black', 'white', 'white', 'white','white']})

# df_1.rename(columns={'product': 'prod'}, inplace=True) 
# df_2.rename(columns={'color_prod': 'color'}, inplace=True)

df = df_1.merge(df_2, how='left', 
                on=['product','color_prod']
                )
df = df_1.merge(df_2, how='inner', 
                on='product',
                suffixes=['shop Left', 'shop_right'], # дает название для одинаковых столбцов из разных датафреймов

                # left_on=['prod','color_prod'],      
                # right_on=['product','color']
                )
print(df)
