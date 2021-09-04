# The `while` loop

The `while` loop in python acts a bit differently than the [`for`](./for.md). While the `for` operates
over the items of an Iterable, the `while` loop acts on a boolean condition.

To be more precise, a `while` loop may be used when the exact number of iterations is unknown. known.

For example, looping until the user gives a valid input:
```python
# uci_bootcamp_2021/examples/while_loops.py
... # code omitted for brevity (see source file in repository)
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:11:26 }}
... # code omitted for brevity (see source file in repository)
```

This example has a decent bit of complexity so let's unpack it a bit.
```python
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:15:16 }}
```
Here we define our `while` loop. We specifically loop while `valid` is False.
 - We don't know how many times the user will give us invalid input; only that the input will be eventually valid given enough iterations.

```python
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:17:18 }}
```
Here we actually prompt the user for an input, using the built-in [`input`](https://docs.python.org/3/library/functions.html#input) function.

> `input()` always returns a `str`ing. To accept an integer, the result of `input` needs to be cast or otherwise parsed.

Speaking of converting the input to a string, that is the next step!

Before we can safetly cast the string to an integer, we should first check that 
the contents of the string is actually numerical.

[`str.isnumeric`](https://docs.python.org/3/library/stdtypes.html#str.isnumeric) returns a boolean, True if the string is nothing but numerical digits.

```python
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:20:22 }}
```

Now that the `result` is an `int`eger, we can do the bounds check.

```python
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:23:24 }}
```

Conversely, if the numerical or bounds checks fail, we should tell the user off!
```python
{{  #include ../../../uci_bootcamp_2021/examples/while_loops.py:25:26 }}
```
> Note that the level of indentation decreased. the `if not valid` is at the same level of indentation as the `if untrusted_input.isnumeric()`!
> 
> Python has significant whitespace!