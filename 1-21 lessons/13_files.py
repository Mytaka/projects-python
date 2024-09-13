file = open('1-21 lessons/13_data/text.txt', 'w') # w - write переписать
# file = open('1-21 lessons/13_data/text.txt', 'a') # a - append добавить

file.write("Hello\n")
file.write("Hello")

file.close()

# ---------------------------------------------------------------------------

file = open('1-21 lessons/13_data/text.txt', 'r') # r - read

# print(file.read(4)) # вывести 4 символа 

for line in file:
    print(line, end="")

file.close()



