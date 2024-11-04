import numpy as np
arr1 = np.arange(15).reshape(3,5)
for row in arr1:
    for cell in row:
        print(cell)
