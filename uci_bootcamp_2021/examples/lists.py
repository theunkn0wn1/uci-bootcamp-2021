"""
# uci_bootcamp_2021/examples/lists.py

Examples on how to use pure-python lists.
"""

# Declaring a list literal.
data = [1, 4, 2, 3]
print(data)
# [1, 4, 2, 3]

# Declaring a list from an Iterable
# `range` is a special Iterable object that generates a sequence of numbers
# between [start, stop), every `step` values.
data = list(range(1, 42, 3))
print(data)
# [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]


# Lists can be sorted, too!
data = [191, 113, 161, 5, 13, 33, 231, 213, 32, 234, 47, 125, 101, 98, 169]
# Simplest possible sort invocation, sorts into ascending order.
data.sort()
# Note: `sort` doesn't return the sorted data: it mutates the data in-place.
print(data)
# [5, 13, 32, 33, 47, 98, 101, 113, 125, 161, 169, 191, 213, 231, 234]

# Sort the data in descending order instead.
data.sort(reverse=True)
print(data)
# [234, 231, 213, 191, 169, 161, 125, 113, 101, 98, 47, 33, 32, 13, 5]


# Items can also be added to the end of the collection.

# NOTE(noinspection): Intentionally writing this in longhand for demonstration purposes.
# noinspection PyListCreation
data = [1, 2, 3]
# Append 4 to the end of the collection
data.append(4)

print(data)
# [1, 2, 3, 4]


# Items can even be mutated in-place.
data[0] = 72
data[1] = data[1] * 4

print(data)
# [72, 8, 3, 4]

# Lists can be mashed together
data2 = [7, 8, 9, 10]
data.extend(data2)
print(data)
# [72, 8, 3, 4, 7, 8, 9, 10]


# Taking the minimum of a list
print(min(data))
# 3

# Taking the maximum of a list
print(max(data))
# 72

# Taking the sum of a list
print(sum(data))
# 121

# Taking the geometric mean of a list
print(sum(data) / len(data))
# 15.125
