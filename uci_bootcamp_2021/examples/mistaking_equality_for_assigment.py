"""
uci_bootcamp_2021/examples/mistaking_equality_for_assigment.py

Demonstrates the common beginner error of mistaking `==` equality for `=` assignment.

WARNING: this file will not run and nor should it be used in any downstream applications,
as it contains intentionally invalid syntax.
"""

# NOTE: Do not mistake the equality operator `==` for the assignment operator `=`

x = 42
y = 42
# Demonstrate comparing two variables by equality
if x == y:
    print("x and y are equivalent!")
else:
    print("x and y are not equivalent!")
z = 17

# NOTE: The following line is erroneous; and is included for demonstration purposes ONLY.
# NOTE: Most linters will throw a warning / error here!
if x = z:
    print("x and y are equivalent!")
else:
    print("x and y are not equivalent!")
