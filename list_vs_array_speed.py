import numpy as np
import time
l1 = [i for i in range(10000000)]
l2 = [i for i in range(10000000)]
a1 = np.arange(10000000)
a2 = np.arange(10000000)
start = time.time()
l3 = [x+y for x,y in zip(l1,l2)]
end = time.time()
print((end-start)*1000)
start = time.time()
result = a1+a2
end = time.time()
print((end-start)*1000)