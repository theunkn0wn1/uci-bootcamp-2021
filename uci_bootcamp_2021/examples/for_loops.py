"""
uci_bootcamp_2021/examples/for_loops.py

Basic examples on how to use for loops in python.
"""
data = [2, 1, 4, 7, 3]

# loop over the items in `data`.
for item in data:
    # `item` refers to the specific element
    # and the body of the for loop runs once per value in `data`.
    print(item)
# 2
# 1
# 4
# 7
# 3

print("-------------")

# We can also for loop over any iterable, such as enumerate!
for i, item in enumerate(data):
    print(i, item)
# 0 2
# 1 1
# 2 4
# 3 7
# 4 3

