import numpy as np

a = np.arange(20)

# slicing
print(a[4:])

print(a[:4])

print(a[5])

s = slice(2, 12, 2) # start, stop, step
print(a[s])

