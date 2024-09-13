# Nikname = input("Tell my your nikname: ")
# Pass = input("Tell my your password: ")


# if Pass != 4 and Nikname == "Mytka":
#     print("Hello Mytka")
# elif Pass >= 10 or Nikname == "Barri":
#     print("Barri lox")
# else: 
#     print("You are imposter")

Pass = input("Tell my your password: ")

Nikname = "Mytka" if Pass == "Barri" else "You are imposter" #Tернарный оператор
print("Your nikname is: ", Nikname)
