import numpy as np

# NUMPY ARITHMETIC OPERATIONS
a = np.arange(9).reshape(3, 3)
print(f"The original array is: ")
print(a)

print()
b = np.array([10, 100, 1000])
print(f"The second array is: ")
print(b)

print()
print(f"The addition of the two arrays is: ")
print(np.add(a, b))  # element-wise addition

print()
print(f"The subtraction of the two arrays is: ")
print(np.subtract(a, b))  # element-wise subtraction

print()
print(f"The multiplication of the two arrays is: ")
print(np.multiply(a, b))  # element-wise multiplication

print()
print(f"The division of the two arrays is: ")
print(np.divide(a, b))  # element-wise division

print()
print(f"The floor division of the two arrays is: ")
print(np.floor_divide(a, b))  # element-wise floor division

