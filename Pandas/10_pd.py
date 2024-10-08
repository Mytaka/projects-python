import numpy as np
import pandas as pd

Indict_array = {'age': [53, np.nan, 11, 18, 7], 
                'паме': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'], 
                         'наличие авто': [True, True, False, np.nan, False],
                         'марка авто': [np.nan, np.nan, np.nan, np.nan, np.nan]}
df = pd.DataFrame(Indict_array)

df.dropna()         # удаляет строки с Nan
df.dropna(axis=1)   # удаляет нужную ось с Nan
df.dropna(how=any,  # удаляет, если есть хотя бы один Nan
          how=all)  # удаляет, если все элементы оси Nan
df.dropna(subset=['age', 'паме']) # удаляет строки, если в укаханых стобцах есть Nan
df.dropna(subset=[1])             # удаляет столбци, елси в указаных строках есть Nan

df.fillna(value=100)              # Nan меняеться на 100
 
                     
df.fillna(value={'age': 100,  
                 'наличие авто': 'еще думает',
                 'марка авто': 'такая беленькая'}) # к каждому столбцу свои требования

df.isna()   # возвращает булевый дадафрейм, в котором Nan - True
df[ ~ df['age'].isna()]

df.notna()  # возвращает булевый дадафрейм, в котором Nan - False

print(df[df['age'].isna()])

