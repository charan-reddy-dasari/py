import numpy as np 
import sys

l = [i for i in range(1000)]
print(len(l)*sys.getsizeof(1))

arr = np.array(l)
print(arr.size*arr.itemsize)