"""
# uci_bootcamp_2021/examples/sets.py

Examples on how to use pure-python sets.
"""

# Declaring a set literal

data = {1, 2, 3}
print(data)
# {1, 2, 3}

# Warning: syntax is VERY similar to dict literal syntax, beware!
some_dict = {}
some_set = set()

print(type(some_dict))
# <class 'dict'>
print(type(some_set))
# <class 'set'>

# Sets only contain unique values, demonstrate this by creating a set from a list with duplicate values.

raw_data = [1, 2, 2, 2, 4, 3, 1, 2, 7]
print(len(raw_data))
# 9

# cast `raw_data` to a set
data = set(raw_data)
# demonstrate that `data` is shorter than the `raw_data` it came from.
print(len(data))
# 5

# and demonstrate that duplicate items are not in the resulting set.
print(data)
# {1, 2, 3, 4, 7}

print("========")

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
# is the same as
print(a | b)
# and it is associative
print(b | a)
# {1, 2, 3, 4, 5}

print(a.intersection(b))
# is the same as
print(a & b)
# and its associative
print(b & a)
# {3}

print(a.difference(b))
# is the same as
print(a - b)
# {1, 2}

print(b.difference(a))
# is the same as
print(b - a)
# {4, 5}
