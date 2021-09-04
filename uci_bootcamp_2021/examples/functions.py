"""
uci_bootcamp_2021/examples/functions.py

examples on how to use functions
"""


def y(x, slope, initial_offset):
    """
    This is a docstring. it is a piece of living documentation that is attached to the function.
    Note: different companies have different styles for docstrings, and this one doesn't fit any of them!

    this is just a small example of how to write a function in python, using simple math for demonstration.
    """
    return slope * x + initial_offset


def y(x: float, slope: float, initial_offset: float = 0) -> float:
    """Same function as above, but this time with type annotations!"""
    return slope * x + initial_offset
