import numpy as np

# resizing arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f'original array:\n{a}')

print(f'The shape of the array is: {a.shape}') # shape of the array

b = np.resize(a, (3, 2)) # resize the array to 3 rows and 2 columns
print(f'\nresized array:\n{b}')
print(f'The shape of the resized array is: {b.shape}') # shape of the resized array 

b = np.resize(a, (2, 3)) # resize the array to 2 rows and 3 columns
print(f'\nresized array:\n{b}')
print(f'The shape of the resized array is: {b.shape}')

b = np.resize(a, (3, 3)) # resize the array to 3 rows and 3 columns
print(f'\nresized array:\n{b}')
print(f'The shape of the resized array is: {b.shape}')
