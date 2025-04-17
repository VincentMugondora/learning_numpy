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

# create a 