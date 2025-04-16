# numpy => is the core library for scientific and numerical computing in python
# it provides high-peformance multidinmensinal array object and tools for working with arrays

import numpy as np

# create a numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)  # [1 2 3 4 5]

# target array values as we do lists
print(a[0])

# numpy is faster than lists
import time
import sys

b = range(1000000)

# memory_used = size_of_one_integer * number_of_integers
print(sys.getsizeof(5)* len(b))  # 28 bytes for each element in the list

c = np.arange(1000000)
print(c.size * c.itemsize)  # 8 bytes for each element in the numpy array

size = 1000000

# lists
L1 = range(size)
L2 = range(size)

# numpy arrays
A1 = np.arange(size)
A2 = np.arange(size)

# time the lists
start = time.time()

# list comprehension to add two lists
# this is the same as L1 + L2
result = [(x + y) for x, y in zip(L1, L2)]
end = time.time()
print(result)
print("Time taken by lists: ", end - start)

# time the numpy arrays
start = time.time()

# this is how we add two numpy arrays
# this is the same as what we did above for lists
# numpy arrays are optimized for performance
result = A1 + A2
# or we can use np.add(A1, A2)

end = time.time()
print(result)
# numpy arrays are faster than lists
print("Time taken by numpy arrays: ", end - start)

