"""
# uci_bootcamp_2021/examples/basic_variables.py
Module containing examples on how to use variables
"""

# Assigning literals to variables.

length = 3
width = 2

# Using variables in expressions, and assigning the result to another variable.
area = length * width

# Using variables in function calls.
print(area)
# 6

# Demonstrating that variables can be re-assigned to different types.
foo = 42
print(type(foo))
# <class 'int'>
foo = "I like pizza."
print(type(foo))
# <class 'str'>
