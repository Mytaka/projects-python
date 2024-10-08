# Сделать флеш картки с использованием пандас и результаты помещать в SQL для аналитики
# (1) - с англ на укр (2) - с укр на англ (3) - с укр на англ но наоборот (4) - с укр на англ но рандом

import numpy as np
import pandas as pd
from time import time

def right_answer(random_num):
    df.loc[random_num, 'right'] = 1

def wrong_answer(df,ukr_word,index,df_words,random_num = None):
    if random_num is None:
        df.loc[index, 'wrong'] = 1
        print('Correct: ', df_words.iat[index,1])
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        if user == '-':
            return '-'
        else:
            return user == df.iat[index,1]
    else:
        df.loc[random_num,'wrong'] = 1
        print('Correct: ',df.iat[random_num,1])
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        if user == '-':
            return '-'
        else:
            return user == df.iat[random_num,1]
    

start_program = time()

ukr = ['задоволений', 'спантеличений', 'схвильований', 'ентузіаст', 'обережний', 'тривожний', 'емоційний зрив', 'наляканий', 'терплячий', 'нетерплячий', 'вдячний', 'веселий', 'везучий', 'настрій', 'отримати', 'перейти дорогу', 'терміновий дедлайн', 'впливати', 'псувати', 'пара', 'відчувати (усі форми)', 'завдання', 'уряд']
eng = ['pleased', 'confused', 'excited', 'enthusiastic', 'cautious', 'anxious', 'emotional breakdown', 'frightened', 'patient', 'impatient', 'grateful', 'cheerful', 'lucky', 'mood', 'to receive', 'to cross the road', 'urgent deadline', 'to influence', 'to spoil', 'couple', 'feel felt felt', 'assignment', 'government']

df = pd.DataFrame({'ukr' : ukr,
                   'eng' : eng,
                   'right': np.nan,
                   'wrong': np.nan,
                   'time' : np.nan,
                   })

flag = input('start(1) | standart(2) | revers(3) | random(4): ')

if flag in ['1','2','3']:
    match flag:
        case '1':
            df_words = df[df.columns[:2:]]
            df_words = df_words[df_words.columns[::-1]]
            print(df_words)
        case '2':
            df_words = df[df.columns[:2:]]
        case'3':
            df_words = df[df.columns[:2:]]
            df_words = df_words.iloc[::-1, :]
            df = df.iloc[::-1, :].reset_index(drop=True)

    for index in range(len(ukr)):
        ukr_word = df_words.iat[index,0]

        start_time = time()
        user = input(f'{index+1}) Translate "{ukr_word}": ')
        end_time = time()
        if user == '-': break
        df.loc[index, 'time'] = round(end_time - start_time,2)

        answer = user == df_words.iat[index,1]

        if answer:
            right_answer(index)
        else:
            res = wrong_answer(df, ukr_word, index, df_words, None)
            if res == '-': 
                break
            else: 
                print(res)

if flag == '4':
    random_nums = np.random.choice(np.arange(0,len(ukr)), size=(len(ukr)), replace=False)
    
    for index in range(len(ukr)):
        random_num = random_nums[index]   # переименовать 'random_num' на 'index'  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ukr_word = df.iat[random_num,0] 
        
        start_time = time()
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        end_time = time()  
        if user == '-': break
        df.loc[random_num,'time'] = round(end_time-start_time,2)

        answer = user == df.iat[random_num,1]

        if answer:
            right_answer(random_num)
        else:
            res = wrong_answer(df, ukr_word, index, None, random_num)
            if res == '-': 
                break
            else: 
                print(res)
print(df)

end_program = time()
print('Finaly time ',round((end_program - start_program),2))