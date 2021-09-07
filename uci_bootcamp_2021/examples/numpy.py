# importing a "secure" pRNG source
# note: the `random` stdlib also exists and would be perfectly applicable here.
#       `secrets` was chosen out of personal preference.
from secrets import randbelow

# Libraries in the SciPy stack tend to shorthand their module names upon import.
# In an effort to be consistent with existing documentation, I will follow that convention.
from typing import FrozenSet

import numpy as np

# Generating some test data
vanilla_list = [randbelow(2 ** 32) for _ in range(500)]

# Declaring an 1d array from the vanilla list.
array = np.array(vanilla_list)

# Taking the sum via vanilla means
print(sum(vanilla_list))
# taking the sum via numpy
print(array.sum())
