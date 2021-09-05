# Comments, String literals, and Docstrings

When writing code, it often helps to leave non-executable notes to anyone who may be reading your code
at a later point in time. This someone includes yourself.

Most languages have the concept of a `comment`, which are non-executable lines embedded into the source
code, which can contain arbitrary text.

> **Code is not self documenting**.

- It is easier to document code as its being written, than trying to figure out what a fragment of code
  is intended to do without documentation at a later point in time.

## Writing comments

In Python, a comment starts with the `#` character. Any text on a given line after `#` is encountered,
is interpreted as a comment.

For example:

```python
# this is a comment, this entire line is ignored by the interpreter.
# print(4 + 4)
# The above line produces no output, since the interpreter ignores it.
print(7 + 3)  # outputs 10.
# the above line runs and doesn't produce a syntax error, since the comment starts where the first `#` in a line is encountered.
```

## Multiline comments

Python does not have multiline comments.

## String Literals

In the [Hello, world!](python/hello_world.md) we made use of a `string literal`.

String literals take one of two primary forms: single line and multi-line.

```python
print("hello world" == 'hello world')
# True


# Multiline strings:
# strings can also be composed of multiple lines

"""
This
is
a
multiline
string
"""

'''
This 
is 
also a
multiline
string
'''
```

