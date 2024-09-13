nums = [5, [5,4,1]]
nums.append(4.5) # добавить в  конец
nums.insert(0,2) # Добавить во внутырь по индексу 0, число 2
a = "Stop"
nums.extend([4,2,1,a]) # добавить в конец масив
nums.sort(key=str) # Сортировать
nums.reverse() # наоборот
nums.pop() # удалить лас елемент
nums.pop(0) # удалить определенный елемент
nums.remove(5) # удалить все 5
nums.clear() # очистить
print(nums)
print(len(nums)) #подсчитать количество символов
print(nums.count(2)) # посчитать количество 2

num = [1,4,5,123,5,2,2,4,5,1]
for i in num:
    i *= 5
    print(i)