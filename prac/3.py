import numpy as np
import pandas as pd
from time import time

start_time = time()

ukr = ['задоволений', 'спантеличений', 'схвильований', 'ентузіаст', 'обережний', 'тривожний', 'емоційний зрив', 'наляканий', 'терплячий', 'нетерплячий', 'вдячний', 'веселий', 'везучий', 'настрій', 'отримати', 'перейти дорогу', 'терміновий дедлайн', 'впливати', 'псувати', 'пара', 'відчувати (усі форми)', 'завдання', 'уряд']
eng = ['pleased', 'confused', 'excited', 'enthusiastic', 'cautious', 'anxious', 'emotional breakdown', 'frightened', 'patient', 'impatient', 'grateful', 'cheerful', 'lucky', 'mood', 'to receive', 'to cross the road', 'urgent deadline', 'to influence', 'to spoil', 'couple', 'feel felt felt', 'assignment', 'government']

df = pd.DataFrame({'ukr' : ukr,
                   'eng' : eng,
                   'right': None,
                   'wrong': None,
                   'time' : None,
                   })


random_nums = np.random.choice(np.arange(0,len(ukr)), size=(len(ukr)), replace=False)
print(random_nums)

user = input('Print: ')
df.loc[random_nums, 'time'] = user

print(df)