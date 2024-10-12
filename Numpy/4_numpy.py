import numpy as np

np_array = np.array([['x','y1'],['x','y'],['x','y'],['x','y']])
np_array1 = np.array([['x','y1'],['x','y'],['x','y'],['x','y']])
np_array2 = np.array([['x','y1'],['x','y'],['x','y'],['x','y'],['x','y']])

new_np = np.expand_dims(np_array, axis=0) # создание нового представления масива с новой осью
new_np = np_array[np.newaxis]             # создание нового представления масива и добавлена нулевая ось
new_np = np_array[ : ,np.newaxis]         # добавлена первая ось
new_np = np_array[ : ,np.newaxis, :]      # добавлена нулевая и вторая оси
new_np = np_array[ ... ,np.newaxis]       # добавлена последняя ось

new_np = np.squeeze(new_np) # удаляет ось с 1 элементом

new_arr = np.hstack([np_array, np_array1])          # объеденяет все масивы в один, но все оси кроме 1 должны совпадать (объеденение по первой оси)
new_arr = np.vstack([np_array,np_array1,np_array2]) # объеденение по 1 оси
new_arr = np.concatenate([np_array,np_array1,np_array2], axis=0) # объеденение по выбраной оси

arr_list = np.array_split(np_array, 2, axis=1)                   # созданет новое представление масива и разделяет масив на списки 

print(arr_list)
print(arr_list[1][0])


