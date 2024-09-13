import numpy as np

np_array = np.array([[[100,2,3,0],[4,5,6,0],[7,8,9,0]],
                     [[1,2,3,0],[4,5,6,0],[7,8,9,0]]])
arr = np_array[0,:] # формирует новое представление масива с помоще среза

# списочная индексация - делает копию масива

# print(np_array[[1,0],[1,2],[3,2]])                                              
# print(np_array[ [ np.array([1,0]) ], [ np.array([1,0]) ], [ np.array([1,0]) ] ])
# print(np_array[ [True,False] ])
index = [ np.array([1,0]) ], [ np.array([1,0]) ], [ np.array([1,0]) ]
index = np.array([[1,0],[1,2],[3,2]])

print(np_array[ [index[0]],[index[1]],[index[2]] ])
