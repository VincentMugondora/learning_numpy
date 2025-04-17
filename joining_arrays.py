import numpy as np

a = np.array([[1,2], [3,4]])
print(f'first array:\n{a}')

b = np.array([[5,6], [7,8]])
print(f'\nsecond array:\n{b}')

# joining two arrays
print(f'\njoining two arrays along axis 0:\n{np.concatenate((a, b))}')

print(f'\njoining two arrays along axis 1:\n{np.concatenate((a, b), axis=1)}')


