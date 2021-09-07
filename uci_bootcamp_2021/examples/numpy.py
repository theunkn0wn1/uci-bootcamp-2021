# importing a "secure" pRNG source
# note: the `random` stdlib also exists and would be perfectly applicable here.
#       `secrets` was chosen out of personal preference.
from secrets import randbelow

import numpy as np

# Libraries in the SciPy stack tend to shorthand their module names upon import.
# In an effort to be consistent with existing documentation, I will follow that convention.

# Generating some test data
vanilla_list = [randbelow(2 ** 32) for _ in range(500)]

# Declaring an 1d array from the vanilla list.
array = np.array(vanilla_list)

# Taking the sum via vanilla means
print(sum(vanilla_list))
# Taking the sum via numpy
print(array.sum())

# Taking the subset of values that are even
evens = array[array % 2 == 0]
# and the equivalent pure-python list:
evens_list = [value for value in vanilla_list if value % 2 == 0]  # "list comprehension"

# multiplying all values of the array by a scalar
double_array = array * 2
double_list = [value * 2 for value in vanilla_list]  # "list comprehension"

# Taking the dot product of two arrays:
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot = v1.dot(v2)
# alternatively,
dot = v1 @ v2
print(dot)

# Note: the pure-python equivalent to this is not clean.
