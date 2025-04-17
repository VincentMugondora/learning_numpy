import numpy as np

# splitting arrays
a = np.arange(9)
print(a)
print(np.split(a, 3)) # split into 3 equal parts
print(np.split(a, [4, 7])) # split at indices 4 and 5

