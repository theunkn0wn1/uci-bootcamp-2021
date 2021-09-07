# Boolean operations and `if` statements

- A [boolean](https://en.wikipedia.org/wiki/Boolean_algebra) a value that is either `True` or `False`.
- A `Boolean expression` is an expression that evaluates to a boolean.

Relational operators, such as `x > y` and `y != z` are boolean expressions.

Booleans are useful for a wide range of applications, from filtering datasets to error handling.

Further, boolean logic underpins the `if` control structure, which allows for *conditional execution*
of statements.

For example, say we have an integer, and we want to know if its even or odd.

```python
# uci_bootcamp_2021/examples/booleans.py:2:9

{{  #include ../../uci_bootcamp_2021/examples/booleans.py:1:9 }}
```

The syntax for `if` is as follows:

```python
if condition:
    ...  # true branch
else:
    ...  # false branch
```

## "Truthiness"

Python has a concept of "Truthy" and "Falsy" values. In effect, all objects have a truth value. For
instance, the integer zero (`0`) is considered "Falsy", while any non-zero integer is "Truthy."

```python
{{  #include ../../uci_bootcamp_2021/examples/booleans.py:12:18 }}
```

All objects have a truth value that is evaluated when that object is treated as a boolean.
- All non-zero numbers are truthy
- All non-empty containers are truthy
- All custom user-types are truthy unless they specifically define a [special method](https://docs.python.org/3/reference/datamodel.html#object.__bool__)

> When python evaluates the `condition` of an `if` statement, it checks for the *truthiness* of the condition.

## the `not` operator
It can also be useful to take the negation of a boolean operation.
This can be achieved via the `not` operator.


```python
{{  #include ../../uci_bootcamp_2021/examples/booleans.py:19:22 }}
```