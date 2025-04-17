import numpy as np

# itrating over an array
print("Iterating over an array")
a = np.arange(0, 45, 5)
a = a.reshape(3, 3)
print(a)

print()
for x in np.nditer(a):
    print(x, end=' ')


# iterating order (C-style or F-style)
print("\n\nIterating order (C-style or F-style)")
print(a)
for x in np.nditer(a, order='C'):
    print(x, end=' ')

for x in np.nditer(a, order='F'):
    print(x)