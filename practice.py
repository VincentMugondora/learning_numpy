import numpy as np
import matplotlib.pyplot as plt

# Numpy practice problems
# 1. Create a 1D array of numbers from 0 to 9
a = np.arange(10)
print("1D array of numbers from 0 to 9:")
print(a)

# 2. Reshape the array into a 2D array with 2 rows and 5 columns
b = a.reshape(2, 5)
print("\nReshaped array (2 rows, 5 columns):")
print(b)

# plot sim graph
x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# create a 6 * 6 two dimensional array and let 1 and 0 to be placed alternatively across diagonals
z = np.zeros((6, 6), dtype=int)
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print("\n6x6 array with 1s and 0s placed alternatively across diagonals:")
print(z)

# find the total number and loactions of missing values in the array
z = np.random.rand(10, 10)
z[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan
print("\nArray with missing values:")
print(z)