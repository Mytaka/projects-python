# my_file = open('Uneversity/Trifles laba 8/name.txt', 'w')
# my_file.write('Nikita Zuev')

# my_file = open('Uneversity/Trifles laba 8/name.txt', 'r')
# print(my_file.read())

# my_file.close()

# -----------------------------------------------------------------------------------------------------------------
# Створити текстовий файл, записати в нього дані, які вводить користувач.  
# Закінченням введення служить порожній рядок. Порахувати та вивести на друк кількість ліній та кількість символів.

# my_file = open('Uneversity/Trifles laba 8/name.txt', 'w')

# user = None
# while True:
#     user = input('Print: ')

#     if user == '':
#         break

#     my_file.write(user + '\n') 
    
# my_file = open('Uneversity/Trifles laba 8/name.txt', 'r')

# lines = my_file.readlines()  # возвращает масив с линиями в документе
# print('lines: ', lines)
# count_lines = len(lines)    
# count_chars = sum(len(line) for line in lines)

# print('count_lines: ',count_lines)
# print('count_chars: ',count_chars)

# my_file.close()

# --------------------------S---------------------------------------------------------------------------------------
# Написати програму яка рахує кількість рядків, які НЕ починаються з літери "T" та кількість рядків, які закінчуються на “d” у файлі poetry.txt. 
# Вивести на друк кількість слів, що починаються з великої літери.

# my_file = open('Uneversity/Trifles laba 8/poetry.txt', 'r')

# T_lines = 0
# lites_d = 0
# words = []

# lines = my_file.readlines()
# for i in lines:
#     if not i.startswith('T'):
#         T_lines += 1
#     elif i[:-1].endswith('d'):
#         lites_d += 1

#     line_words = i.split(' ')
#     for j in line_words:
#         if j == j.capitalize():
#             words += [j]

# my_file.close()

# print(T_lines)
# print(lites_d)
# print(len(words))

# -----------------------------------------------------------------------------------------------------------------
# У файлі mbox-short.txt порахувати кількість символів в кожному рядку файлу та знайти найдовше слово.

# import pandas as pd

# file = open('Uneversity/Trifles laba 8/mbox-short.txt', 'r')
# lines = file.readlines()

# line_chars = []
# longest_word = '0'

# for i in lines:
#     line_chars += [len(i)]

#     words = i.split(' ')
#     for j in words:
#         if len(longest_word) <= len(j):
#             longest_word = j
# file.close()

# ser = pd.Series(line_chars,
#                 index=[f'line_{i}' for i in range(1,len(lines)+1)],
#                 name='line_chars',)

# print(ser)
# print('longest_word: ',longest_word)

# ----------------------------------------------------------------------------------------------------------------- 
# Напишіть програму яка зчитує файл mbox-short.txt та друкує його вміст (рядок за рядком) у верхньому регістрі. 
# Виконання програми буде виглядати наступним чином: 

# file = open('Uneversity/Trifles laba 8/mbox-short.txt', 'r')
# lines = file.readlines()
# file.close()

# for i in range(0,5):
#     print(lines[i].upper().rstrip())

# -----------------------------------------------------------------------------------------------------------------
#  Написати програму, яка відкриває файл mbox-short.txt, виводить на друк усі рядки, що містять значок «@» та рахує їх кількість.

# file = open('Uneversity/Trifles laba 8/mbox-short.txt', 'r')
# lines = file.readlines()
# file.close()

# count_line_w_sign = 0
# for i in lines:
#     if '@' in i:
#         count_line_w_sign += 1
#         print(i.rstrip())
# print('\ncount_line_w_sign: ', count_line_w_sign)

# -----------------------------------------------------------------------------------------------------------------
# Написати програму, яка з файлу 'feedback.txt' переписує у файл ‘positive.txt’ всі позитивні відгуки, а у файл ‘negative.txt‘ усі негативні відгуки. 
# У файлі feedback_analysis.txt вивести інформацію про загальну кількість відгуків, кількість позитивних та кількість негативних відгуків 

# my_file = open('Uneversity/Trifles laba 8/feedback.txt', 'r')
# lines = my_file.readlines()
# my_file.close()

# positive_count = 0
# negative_count = 0

# for i in lines:
    
#     if i.strip().startswith('Positive'):
#         with open('Uneversity/Trifles laba 8/positive.txt', 'a') as file:
#             file.write(i)
#         positive_count += 1

#     elif i.strip().startswith('Negative'):
#         with open('Uneversity/Trifles laba 8/negative.txt', 'a') as file:
#             file.write(i)
#         negative_count += 1
    
# feedback_count = len(lines)

# file = open('Uneversity/Trifles laba 8/feedback_analysis.txt', 'w')
# file.write(f'positive_count: {positive_count} \nnegative_count: {negative_count} \nfeedback_count: {feedback_count}')
# file.close()       

# with open('Uneversity/Trifles laba 8/feedback_analysis.txt', 'r') as analys:
#     print(analys.read())


