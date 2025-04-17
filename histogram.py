import numpy as np
import matplotlib.pyplot as plt

a = np.array([20, 87, 4, 40, 53, 74, 56, 51, 11, 20, 40, 15, 79, 25, 27])
 # Generate 1000 random numbers from a normal distribution
plt.hist(a, bins = [0, 20, 40, 60, 80, 100])
plt.title('Histogram')
plt.show()
# This code generates a histogram of 1000 random numbers drawn from a normal distribution.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)         # Line plot
plt.title("My Chart")  # Chart title
plt.xlabel("X-Axis")   # X-axis label
plt.ylabel("Y-Axis")   # Y-axis label
plt.show()             # Show the plot
