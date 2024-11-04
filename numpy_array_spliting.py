import numpy as np
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
result = np.hsplit(arr1,2)
result2 = np.vsplit(arr1,2)
for i in result:
    print(i)

for i in result2:
    print(i)