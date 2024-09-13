import numpy as np

arr = np.arange(2*3*3).reshape(2,3,3)

np.random.rand() # возвращает рандомное число [0;1)
np.random.rand(4) # возвращает масив с рандомными числами
np.random.rand(4,2) # возвращает масив с рандомными числами

np.random.randn() # возвращает стандартного нормального распределения (среднее значение 0, стандартное отклонение 1)
np.random.randn(4)
np.random.randn(4,2)

np.random.normal(5,10) # нормальное распределение с 5 - средним значением и 10 - стандартным отклонением
np.random.normal(5,10, 100) # где 100 - количество
np.random.normal(5,10, [4,2])

np.random.randint(5) # возвращает нормальное равномерное распределение [0;5)
np.random.randint(4,2) 
np.random.randint(4,2, size=(4,2)) 

np.random.choice([1,2,3,4,5], 10) # возвращает равномерно рандомно взятые числа с масива

np.random.shuffle(arr) # перемешивает масив в доль нулевой оси

np.random.seed(42) # создает сид, для рандома
a = np.random.rand(4,2)

print(a)

