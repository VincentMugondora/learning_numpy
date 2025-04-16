# numpy basic operations
import numpy as np

a = np.array([[1,2], [3,4], [5,6]])
print(a)
print(a.ndim)  # number of dimensions
print(a.itemsize)  # size of each element in bytes
print(a.shape)  # shape of the array
print(a.size)  # number of elements in the array

a = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
print(a)
print(a.itemsize)  # size of each element in bytes
print(a.shape)

a = np.array([[1,2], [3,4], [5,6]], dtype=np.complex64)
print(a)
