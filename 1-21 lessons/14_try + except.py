# x = " "
# while x == " ":
#     try:
#         x = int(input("Tell me any number: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Tell me NUMBER matherfacker") 

x = "hello"
while x == "hello":
    try:
        a = int(input("Tell my first number: "))
        b = int(input("Tell me second number: "))
        x = a/b
        print(x)
    except ValueError:
        print("Tell me NUMBER matherfacker")
    except ZeroDivisionError:
        print("We cannot divide by zero, IDIOT")
    else: 
        print("WOW, On the first try, i don't expect it")
    finally:
        print("Well done stupid")
        

