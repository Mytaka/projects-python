import numpy as np

np.random.seed(42)

arr_1 = np.random.randint(10,size=[2,3,2])
arr_2 = np.arange(2,8).reshape([3,2])

print(arr_1 == 1) # ==  !=  <  > <= >=
print(arr_1[arr_1 == 1]) # выводит только подходящие под условие элементы
arr_1 == [3,7]

np.greater(arr_1,arr_2) #       - > 
np.greater_equal(arr_1,arr_2) # - >= 
np.less(arr_1,arr_2) #          - < 
np.less_equal(arr_1,arr_2) #    - <= 
np.equal(arr_1,arr_2) #         - == 
np.not_equal(arr_1,arr_2) #     - 1=

# согласованые масивы так же сравниваються !!!!

print( arr_1 == arr_2.reshape([1,3, 2]) )
print( arr_1 < arr_2[:, np.newaxis, np.newaxis] )

# ------------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5])

print( arr < 6 )
print( np.all(arr < 6) ) # вернет True <==> весь масив True

print( arr < 2 ) 
print( np.any(arr < 2) ) # вернет True <==> хотя бы один элемент True

