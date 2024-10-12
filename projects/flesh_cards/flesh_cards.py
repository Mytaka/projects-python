import numpy as np
import pandas as pd
import sqlite3 as sq
from time import time
from datetime import datetime
from IPython.display import clear_output


def right_answer(random_num):
    df.loc[random_num, 'right'] = 1

def wrong_answer(df,ukr_word,index,df_words,random_num = None, flag = None):
    if random_num is None:
        df.loc[index, 'wrong'] = 1
        print('Correct: ', df_words.iat[index,1])
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        if user == '-':
            return '-'
        elif flag == 1:
            return user == df_words.iat[1,index]
        else:
            return user == df_words.iat[index,1]
    else:
        df.loc[random_num,'wrong'] = 1
        print('Correct: ',df.iat[random_num,1])
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        if user == '-':
            return '-'
        else:
            return user == df.iat[random_num,1]
    
def db_end_mean(db_data,df_db):
    print('-------------------------------------\nAttempt counter: ',int(len(db_data)/len(ukr)))     

    end_ser = ~df_db['end_program'].duplicated()
    print('Attempt everage time:', round(df_db['end_program'][end_ser].agg('mean'),2), 'seconds')
    

start_program = time()

ukr_22 = ['помітити', 'досвід', 'терпіння', 'винний', 'чесний', 'скоріше', 'обіймати', 'розгадати', 'загадковий', 'колега', 'алкоголь']
eng_22 = ['to notice', 'experience', 'patience', 'guilty', 'honest', 'rather', 'hug', 'to puzzle', 'puzzling', 'colleague', 'alcohol']

ukr = ukr_22
eng = eng_22

df = pd.DataFrame({'ukr' : ukr,
                   'eng' : eng,
                   'right': 0,
                   'wrong': 0,
                   'time' : np.nan,
                   'end_program': np.nan,
                   'date': np.nan
                   })

today = datetime.now()
formatted_date = today.strftime("%d-%m-%Y")
df['date'] = formatted_date


flag = input('start(1) | standart(2) | revers(3) | random(4): ')

if flag in ['1','2','3']:
    match flag:
        case '1':
            df_words = pd.DataFrame(df,
                                    columns=['eng','ukr'])
        case '2':
            df_words = df[df.columns[:2]]
        case'3':
            df_words = df[df.columns[:2]]
            df_words = df_words.iloc[::-1, :]
            df = df.iloc[::-1, :].reset_index(drop=True)

    for index in range(len(ukr)):
        ukr_word = df_words.iat[index,0]

        start_time = time()
        user = input(f'{index+1}) Translate "{ukr_word}": ')
        end_time = time()
        if user == '-': break
        df.loc[index, 'time'] = round(end_time - start_time,3)

        answer = user == df_words.iat[index,1]

        if answer:
            right_answer(index)
        else:
            res = wrong_answer(df, ukr_word, index, df_words, None, flag)
            if res == '-': 
                break
            else: 
                print(res)

if flag == '4':
    random_nums = np.random.choice(np.arange(0,len(ukr)), size=(len(ukr)), replace=False)
    
    for index in range(len(ukr)):
        random_num = random_nums[index]   
        ukr_word = df.iat[random_num,0] 
        
        start_time = time()
        user = input(f'{index+1}) Translate "{ukr_word}" ')
        end_time = time()  
        if user == '-': break
        df.loc[random_num,'time'] = round(end_time-start_time,3)

        answer = user == df.iat[random_num,1]

        if answer:
            right_answer(random_num)
        else:
            res = wrong_answer(df, ukr_word, index, None, random_num)
            if res == '-': 
                break
            else: 
                print(res)

end_program = time()
finish_time = round((end_program - start_program),3)
df['end_program'] = finish_time

with sq.connect('data.db') as db: # 23 in one df, 7 in one tuple 
    c = db.cursor()

    # c.execute('DROP TABLE IF EXISTS data')                             # Заміняти тут і нижче

    c.execute('''CREATE TABLE IF NOT EXISTS words_22 (
              "index" INTEGER,
              ukr TEXT,
              eng TEXT,
              right TEXT,
              wrong TEXT,
              time FLOAT,
              end_program FLOAT,
              date TEXT
              )''')     
    
    df.to_sql('words_22', db, if_exists='append', index=True)            # Заміняти тут
    c.execute('SELECT * FROM words_22')                                  # Заміняти тут 
    db_data = c.fetchall()

    db.commit()

db_arr = np.array(db_data, dtype=object)

arr_index, arr_ukr, arr_eng, arr_right, arr_wrong, arr_atime, arr_end_program, arr_date = map(list, zip(*db_arr))

df_db = pd.DataFrame({'index':arr_index,
                      'ukr' : arr_ukr,
                      'eng' : arr_eng,
                      'right': arr_right,
                      'wrong': arr_wrong,
                      'time' : arr_atime,
                      'end_program': arr_end_program,
                      'date': arr_date
                      })

df_db = df_db.dropna(subset=['time'])

df_db = df_db.astype({'time' :  np.float64,
                      'end_program': np.float64,
                      'date': 'datetime64[ns]'})
df_db['right'] = pd.to_numeric(df_db['right'], downcast='integer', errors='coerce').astype(np.int64)
df_db['wrong'] = pd.to_numeric(df_db['wrong'], downcast='integer', errors='coerce').astype(np.int64)

clear_output(wait=True)
print(df[['ukr','eng','right','wrong','time']])
print('Results : ', df['right'].sum(), '|', df['wrong'].sum())
print('Time: ', finish_time)

while True:
    user = input('Global analytics(1) | dates analytics(2): ')

    if user == '-':
        break

    elif user == '1':
        clear_output(wait=True)
        groups = df_db.groupby(['index','ukr', 'eng',], as_index=True).agg({
            'right': 'sum',
            'wrong': 'sum',
            'time': 'mean', 
        })
        print(groups[['right','wrong','time']])
        db_end_mean(db_data,df_db)

    elif user == '2':
        clear_output(wait=True)

        groups = df_db.groupby(['date'], as_index=True).agg({
            'right': 'sum',
            'wrong': 'sum',
            'time': 'mean', 
        },)
        end_ser = ~df_db['end_program'].duplicated()
        groups['All time'] = round(sum(df_db['end_program'][end_ser])/60,2)
        print(groups)

        db_end_mean(db_data,df_db)