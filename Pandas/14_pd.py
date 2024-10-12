import numpy as np
import pandas as pd

dct = { f'col_{i}': [i*1, 1*2, 1*3, 1*4, i*5] if i != 3 else [i, i, i, i, i] for i in range(5)}

df = pd.DataFrame(dct)

df.apply(np.min,               # сама функцыя
         axis=0,               # по какой оси будет эта функцыя
         raw=False,            # если raw = True - данные будут передаваться как масив нампай, а не датафрейм
                               # если передавать ка к датафрейм, то робота будет проводится с каждой серией, а если масив то со всем масивом сразу
         result_type='expand', # разделяет столбец на столбци ( "слово0, слово1" ) = ("слово0")("слово1")
         args=(a,b,c,d),       # фактические параметры
         **kwargs)             # формальные параметры
# Series.apply(func, args(), **kwargs)

df.apply(np.min)  # возвращает таблицу с заданой функцией

def my_fanc(Series):
    return ( Series + 100 ) if Series.name != 'col_2' else ( Series * 0 )
df.apply(my_fanc)

df.apply(lambda Series: ( Series + 100 ) if Series.name != 'col_2' else ( Series * 0 ))


