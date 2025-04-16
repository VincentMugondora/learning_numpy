import numpy as np

# changing shape of an array

a = np.arange(9)
print(f"The original array is: {a}")

# we want this to reshape array a
b = a.reshape(3, 3)
print(f"The reshaped array is: {b}")

# flatten the array
print(b.flatten(order='F')) 

# reshape the array
print()
print("reshaping the array")
a = np.arange(12).reshape(3, 4)
print(a)

# transpose the array
print()
print("transpose the array")
print(np.transpose(a))  

# created another array named b and reshaped it to 2x4
print()
print("reshaping the array")
b = np.arange(8).reshape(2, 4)
print(b)

print()
c = b.reshape(2,2,2)
print(c)

print()
print(np.rollaxis(c,2))

print()
print("Swap axes")
# print(np.swapaxes(c, 0, 2))
print(np.swapaxes(c, 1, 2))