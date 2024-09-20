import numpy as np
import pandas as pd

df = pd.read_csv('Trifles/table.csv')
df_copy = df.to_csv('Trifles/avito.csv',        # загрузить в папку 
                    sep=',',                    # выбираем будет раздедитель
                    columns=['date1','date2'],  # какие колонки сохранять
                    header=True,                # сохранять ли заголовок
                    header=['Month','Days'],    # задает имена заголовкам колонок
                    index = True,               # сохраняються ли индексы 
                    index_label='index_row',    # задает заголовок индексам
                    encoding='utf8'             # кодировка
                    )        


