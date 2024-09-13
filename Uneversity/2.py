# def text_4(text):
#     while not text.startswith('Programming'):
#         text = text[1:]
#     while not text.endswith('Programming'):
#         text = text[:-1]
#     return text

# text = 'PythonProgrammingIsFun'
# res1 = text
# res2 = text[6:]
# res3 = text[:7]
# res4 = text_4(text)
# res5 = text[-5:-1]
# res6 = text[::3]
# res7 = text[6:15:2]
# res8 = text[::-1]
# res9 = len(text)
# results = [res1, res2, res3, res4, res5, res6, res7, res8, res9]

# for i in range(0,len(results)):
#     print(f'{i} {results[i]}')

# -------------------------------------------------------------------------------------------------

# text = input ( "Введіть рядок: " )
# print(len(text))

# -------------------------------------------------------------------------------------------------

# text = input ( "Введіть рядок: " )
# res = text.count(' ')
# print(res+1)

# -------------------------------------------------------------------------------------------------

# text = 'Find the position of Python'
# res = text.find('Python')
# print(res)

# -------------------------------------------------------------------------------------------------

# numeric_string = '12345'
# res = numeric_string.isdigit()
# print(res)

# -------------------------------------------------------------------------------------------------

# text = 'make this uppercase'
# res = text.upper()
# print(res)

# # -------------------------------------------------------------------------------------------------

# filename = 'example.txt'
# res = filename.startswith('example')
# print(res)

# # -------------------------------------------------------------------------------------------------

phone = '+38(099)-123-12-13'
res = phone.replace('(', '')
res = res.replace(')', '')
res = res.replace(' ', '')
res = res.replace('+', '')
print(res)

