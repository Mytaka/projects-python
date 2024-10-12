import numpy as np

np_array = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0]])

np_array.shape = (2,2,3)  # меняет размеры уже существующего масива или возвращает их
np_array.reshape([2,2,3]) # создает новый масив с теми же данными но новыми размерами
np_array.resize((4,4), refcheck=True) # меняет размеры малива
np_array.ravel() # любой масив делает одномерным

np_new_array = np_array.ravel().copy() # создает для данных масива отдельную ячейку памяти
np_new_array[0]=222

print( np_array, end= '\n\n')
print(np_new_array)
