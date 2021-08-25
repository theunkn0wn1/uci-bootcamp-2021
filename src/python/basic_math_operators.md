# Basic Math Operators

Now that "hello world" is out of the way, let's do some maths.

Python has the standard complement of mathematical operators for addition, subtraction, multiplication,
and both integer/floating point division operators. Beyond these, there is a selection of standard
library [math](https://docs.python.org/3.8/library/math.html) components, which are greatly expanded on
by third-party libraries. [more on those later](third_party_libs/readme.md)

## Addition

```python
print(4 + 3)
# 7
print(-6 + 4 + 2)
# 0
```

## Subtraction

```python
print(12 - 5)
# 7
print(-5 - 7)
# -12
```

## Multiplication

```python
print(22 * 4)
# 88
```

## Division

```python
print(22 / 2)
# 11.0
print(5 / 6)
# 0.8333333333333334
# Note: Exact output may vary slightly.
```

## Integer Division

`/` refers to "floating point" division, and produces a decimal output.

```python
print(type(5 / 6))
# <class 'float'>
```

There are cases where an integer output is instead desirable. For this, python has a second division
operator:

```python
print(5 // 6)
# 0
print(type(5 // 6))
# <class 'int'>
```

## Modulus

The last of the core math operators we will introduce at this point is the modulus operator.

```python

print(15 % 6)
# 3
print(15 // 6)
# 2
```

> Note: The modulus of `i % j` will have the same sign as `j`.