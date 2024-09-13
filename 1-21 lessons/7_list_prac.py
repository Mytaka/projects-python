# пользователь вводит данные в масив и зополняет его
b = int(input("How many numbers do you want? "))
num = []
for i in range(0,b):
    user = input("Give my any number: ")
    num.append(user)
print(num)

num = []
user = 0
while user != "Stop":
    user = input("Give my any number: ")
    num.append(user)
    print("You can add more numbers ot say Stop" )
num.pop()
print(num)

num = []
i = 1
n = int(input("How many numbers do you want to safe? "))
while i < n:
    string = "number №" + str(i) + ":"
    num.append(input(string))
    i += 1
print(num)