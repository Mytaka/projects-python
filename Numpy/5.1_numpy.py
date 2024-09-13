import numpy as np

data = np.empty([1000,28,28])
arr_1 = np.empty([50,28,28])
arr_2 = np.empty([28,28])

new_data = np.append(data, arr_1) # создает копию масива с доп. элементами
new_data = np.append(data, arr_1, axis=0) # создает копию масива с доп. элементами по определенной оси, но нужно что бы остальные оси совпадали
new_data = np.append(data, arr_2[np.newaxis], axis=0)

new_data = np.delete(new_data, 1, axis=0)

print(new_data.shape)
