import numpy as np
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[2,3],[4,6],[7,8]])
arr3 = np.vstack((arr2,arr1))
print(arr3)
