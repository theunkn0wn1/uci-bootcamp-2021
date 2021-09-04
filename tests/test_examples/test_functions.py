# Comparing floats can only be done imprecisely
from math import isclose

# Bring the function defined in the example into scope.
from uci_bootcamp_2021.examples.functions import y


def test_y():
    result = y(42, 0.5, 0)

    # Note: cannot compare floats by equality; given floating point inaccuracy.
    # Here we assert that 21.0 is close to the output of the function given known inputs.
    assert isclose(result, 21.0)


def test_y_kwargs():
    result = y(x=42, initial_offset=0, slope=0.5)
    # Note: cannot compare floats by equality; given floating point inaccuracy.
    # Here we assert that 21.0 is close to the output of the function given known inputs.
    assert isclose(result, 21.0)