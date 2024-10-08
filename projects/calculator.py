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