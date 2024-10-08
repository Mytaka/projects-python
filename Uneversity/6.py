# import time
# import numpy as np

# time1 = []
# time2 = []
# while len(time2) < 10:
#     start_time = time.time()  # Запоминаем текущее время

#     def calculate_profit(amount,percent,period):
#         res = [amount]

#         if (amount or percent or period) == 0:
#             return 0

#         for i in range(1,period+1):
#             res.append( res[i-1] + res[i-1]*percent/100 )
#         return round(res[period] - amount)

#     end_time = time.time()  # Время после выполнения кода
#     execution_time1 = end_time - start_time  # Разница - время выполнения
#     time1 += [execution_time1]

#     print(calculate_profit(1000, 5, 1) == 50)
#     print(calculate_profit(12500,3,12) == 5322)
#     print(f"Время выполнения: {execution_time1:.6f} секунд")
#     # ----------------------------------------------------

#     start_time = time.time()

#     def calculate_profit(amount,percent,period):
#         if (amount or percent or period) == 0:
#             return 0

#         for i in range(period):
#             res = amount * (1+ percent / 100) ** period
#         return round(res - amount)

#     end_time = time.time()  # Время после выполнения кода
#     execution_time2 = end_time - start_time  # Разница - время выполнения        
#     time2 += [execution_time2]

#     print(calculate_profit(1000, 5, 1) == 50 ) 
#     print(calculate_profit(12500,3,12) == 5322)
#     print(f"Время выполнения: {execution_time2:.6f} секунд")

# print('time1 = ', time1)
# print('time2 = ', time2)

# ------------------------------------------------------------------------------

# result — сюди поміщаємо підсумковий результат 
# operand — завжди зберігає поточне число 
# operator — рядковий параметр, може містити чотири значення, "+", "-", "*", "/" 
# wait_for_number — прапорець, який вказує, що очікують на вводі оператор (operator) або операнд (operand)

# operand = None
# operator = None

# operand = (input('Print any number: '))
# while not str(operand).isdigit():
#         print('Operend is not numeric')
#         operand = (input('Print any number: '))
# operand = int(operand)

# while operator != '=':
#     try:
#         match operator:
#             case '+':
#                 operand += int(input('Print any number: '))
#             case '-':
#                 operand -= int(input('Print any number: '))
#             case '*':
#                 operand *= int(input('Print any number: '))
#             case '/':
#                 operand /= int(input('Print any number: '))
#     except ZeroDivisionError:
#         print('Division by zero is not allowed!')
#         continue
#     except (TypeError, ValueError):
#         print('Operend is not numeric')
#         continue

#     operator = input('Print any sign: ')
    
#     if operator not in ['+', '-', '*', '/', '=']:
#         print('Must be [+] or [-] or [*] or [/] or [=]')

# print(operand)

# ------------------------------------------------------------------------------

result = None
operand = None
operator = None
wait_for_number = True

def find_operand():
    global wait_for_number
    wait_for_number = True

    while wait_for_number:
        operand = input('Print any number: ')
        if operand.isdigit(): 
            wait_for_number = False
            operand = int(operand)
            return operand
        else:
            print('Operand is not numeric')
    
result = find_operand()

while not wait_for_number:
    try:
        match operator:
            case '+':
                result += find_operand()
            case '-':
                result -= find_operand()
            case '*':
                result *= find_operand()
            case '/':
                result /= find_operand()
    except ZeroDivisionError:
        print('Division by zero is not allowed!')
        continue

    operator = input('Print any sign: ')
    
    if operator not in ['+', '-', '*', '/', '=']:
        print('Must be [+] or [-] or [*] or [/] or [=]')
    elif operator == '=':
        break
    
print(result)
