import numpy as np
import time

start_time = time.time()

# arr = np.empty([1000,28,28])
# for i in arr:
#     img = np.random.randint(0,255,28*28).reshape([28,28]) 
#     arr = np.append(arr, img[np.newaxis], axis=0)

arr = np.empty([1000,28,28])
arr.resize([2000,28,28])

for i in range(1000):
    img = np.random.randint(0,255,28*28).reshape([28,28])
    arr[1000+i] = img

end_time = time.time()

print(end_time - start_time)

# 3.11 sec
# 0.026 sec