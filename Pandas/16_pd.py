import numpy as np
import pandas as pd

df = pd.DataFrame({'Имя': ['name_1', 'name_2', 'name_3', 'name_3', 'name_3', 'name_2', 'name_4'], 
                   'Город работы': ['city_1', 'city_2', 'city_3', 'city_3', 'city_4', 'city_1', np.nan], 
                   'Как_долго_работал': [12, 24, 36, 12, 48, 5, np.nan]})

groups = df.groupby(['Имя', 'Город работы'])  # возвращает генератор
for name,group in groups:
    print(name)
    print(group)

sum_group = df.groupby('Город работы').sum()               # возвращает датафрейм с сумой значений в группе
sum_group = df.groupby('Город работы', as_index=False      # as_index - будут ли отображаться имена групп в виде столбца
                       ).sum()

# !!! для групирования конкретных данных !!!
# df.groupby( колонка/колонки для группировки, ...)[ столбец/столбцы ]. метод агригации ()

group = df.groupby('Имя')[ 'Как_долго_работал' ].sum()   # сума "Как_долго_работал"
group = df.groupby(['Имя', 'Город работы']).count()      # сколько раз работал

group = df.groupby(['Имя', 'Город работы'], dropna=False) \
          .count() \
          .rename(columns={'Как_долго_работал' : 'count'}) # сколько раз в городе работал сотрудник

group = df.groupby('Имя')['Город работы'].nunique()              # в скольких городах работал сотрудник
group = df.groupby ("Имя").agg({'как_долго_работал': np.sum})    # как долго сотрудник работал
group = df.groupby('Имя').agg({'Город работы': 'count', 
                               'Как_долго_работал': [np.sum, np.max]}) # сколько раз работал, сколько работал, 
                                                                       # максимальное рабочее время на одном месте
# !!! именованая агрегация !!!
group = df.groupby('Имя', as_index=False).agg( count_jobs=('Город работы', 'count'), 
                                               experience=('Как_долго_работал', 'sum'))
print(group)

