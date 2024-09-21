# text_pass = "hhh lll hhh ddd sss"
# passes = text_pass.split(' ')
# my_pass = 'dddd'

# for i in range(0,len(passes)):
#   if passes[i] == my_pass:
#     print(passes[i], ' index = ',i)
#   elif i == (len(passes)-1):
    #  print("пароля у списку немає")

# ---------------------------------------------------------------------------

# a = int(input('print any number: '))
# b = int(input('print any number: '))
# c = int(input('print any number: '))
# res = [a,b,c]
# print(max(res))

# ---------------------------------------------------------------------------

# days = {1: "Понеділок",2: "Вівторок",3: "Середа",4: "Четвер",5: "П'ятниця",6: "Субота",7: "Неділя"}
# number = input('Напиши номер дня тижня:')
# print(days[number])

# ---------------------------------------------------------------------------

# user_age = int(input('How old are you? '))
# if user_age <= 18:
#   print('Ви вважаєтеся Здоровим.')
# elif user_age > 18:
#         user_illness = int(input('порахуй, скільки перерахованих пунктів про тебе: супутні захворювання, паління, вживання алкоголю: '))
#         if user_illness == 0:
#           print('Ви вважаєтеся Здоровим.')
#         elif user_illness > 0:
#           print('Ви вважаєтеся в зоні ризику')

# ---------------------------------------------------------------------------

print("Ласкаво просимо до банкомату!") 
print("Виберіть дію:") 
print("1. Перевірити баланс") 
print("2. Внести гроші") 
print("3. Зняти гроші") 
print("4. Вихід")

balance = 100 #$

while True:
    user = int(input('Оберіть дію: '))
    if user == 1:
        print(balance,'$')

    elif user == 2:
        while balance:
            input_money = float(input('скільки грошей ви хочете внести? '))
            if input_money > 0:
                balance += input_money
                print('Операція пройшла успішно')
                print('Ваш баланс: ', balance,'$')
                break
            else:
                print('Введіть число більше за нуль')
    
    elif user == 3:
        if not balance:
            print('У вас порожній баланс ＞﹏＜') 
        while balance:
            output_money = float(input('скільки грошей ви хочете зняти? '))
            if output_money >= 0 and output_money <= balance:
                balance -= output_money
                print('Операція пройшла успішно')
                break
            elif output_money < 0:
                print('Введіть число більше за нуль')
            elif output_money > balance:
                print('Введіть число менше за ваш баланс')
            print('Ваш баланс: ', balance,'$')
          
    elif user == 4:
        break
print('Дякуємо за довіру')