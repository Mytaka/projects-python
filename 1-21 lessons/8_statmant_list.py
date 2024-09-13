word = 'Hello world'
print(word[1])
print(len(word)) # подсчитть количество символов

print(word.upper()) # меняет регистр на верхний у всей страки
print(word.lower()) # меняет регистр на нижний у всей страки
print(word.isupper()) # проверяет на верхний регистр у всей страки
print(word.islower()) # проверяет на нижний регистр у всей страки
print(word.capitalize()) # делает верхний регистр для первого символа строки, а для остальных символов делает в нижнем
print(word.find("o")) # даёт индекс первого совпадающего елемента
print(word.split(" ")) #разделяет список по символу

# создать где мы будем обращаться к каждому слову в страке и делать для него capitalaze

statmant = "super car is fantastic"
words = statmant.split(" ")
el = int(statmant.count(" "))
el += 1
i=0
print("Result: ", end="")
for i in range(0,el):
    capitalize = words[i].capitalize()   
    print(capitalize, end=" ")

statmant = "super car is fantastic"
words = statmant.split()
for i in range(0,len(words)):
    words[i].capitalize
# print(words)
result = " ".join(words)
print(result)


