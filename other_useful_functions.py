import numpy as np

# other useful functions in numpy

# linspace function
a = np.linspace(1, 3, 10) # start, stop, number of samples
print(f'linspace function:\n{a}')

# sum and axis
a = np.array([(1,2,3), (4,5,6)])
print(f'\nsum function:\n{a.sum(axis=0)}')

# square root and standard deviation
print(f'\nsquare root function:\n{np.sqrt(a)}')
print(f'\nstandard deviation function:\n{np.std(a)}')

# ravel function
a = np.array([[1,2,3], [4,5,6]])
print(f'\nravel function:\n{a.ravel()}')

# logarithm function
a = np.array([1, 10, 100])
print(f'\nlogarithm function:\n{np.log10(a)}')
print(f'\nlogarithm function:\n{np.log(a)}')
