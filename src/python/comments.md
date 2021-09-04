# Comments, String literals, and Docstrings

When writing code, it often helps to leave non-executable notes to anyone who may be reading your code
at a later point in time. This someone includes yourself.

Most languages have the concept of a `comment`, which are non-executable lines embedded into the source
code, which can contain arbitrary text.

> **Code is NOT self documenting**.

While you may understand what you wrote at the time you did so, returning to the code at a later point
in time, you may forget the context, intent, or implementation details over time. Comments are a form
of documentation. Do yourself and anyone that ends up reading your code a favor and use comments to
document your code as you write it.

- It is easier to document code as its being written, than trying to reverse-engineer the code in post
  without that documentation.

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

## Docstrings

The `Docstring` is a concept related to `comments` insofar as both are forms of documentation.

When you write a [Module](python/modules.md) or [Function/Method](python/functions.md), it is best
practice to write some documentation explaining what that module/function/method is doing.

A Docstring is a string literal that is attached to the Module/Function/Method, and it is read and
handled by the interpreter. It serves as that object's human-readable documentation.

- For a Module, the docstring should be on the first line of executable code, only below comments and
  above imports.
- For functions and methods, the docstring should be the first line of executable code within the
  function/method body.
- Stylistically, docstrings should use the multiline string format.

## Example formats

For the remainder of this document, all executable code examples will include a module string that
contains:

- the path to the example in the git repository
- a brief explanation of the example module

> For pages in this document that cite the same example, but render different lines of that example, the docstring will only be rendered in the first example codeblock to limit repetition.

