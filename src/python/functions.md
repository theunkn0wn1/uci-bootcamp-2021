# Functions and methods

Thus far we've covered many primitive python operations, as well as called many `functions`, its past
due to talk about what a function is.

In simple terms: a function is a re-usable piece of code. It is one of the core building blocks of
abstraction, allowing complex implementation details to be hidden away behind simple function call
syntax.

## Syntax.

the `def` keyword is used to define functions and methods. The minimum syntax is as follows:

```python
def some_function():
  ...  # inside `def some_function()`
# outside def some_function()
```

Like all control structures, the *body* of the function is denoted using indentation.

For a function to be re-usable, there are generally bits of data that need to be provided for the
function to do anything useful.

Let's start with the geometric function that defines a line, `y=mx+b`.

```python
{{  #include ../../uci_bootcamp_2021/examples/functions.py:1:15 }}
```

A function is composed of three parts:

- the function signature contains the `def {{name}}({{parameters}}):`
- the function's docstring contains documentation of the function itself, such as what the function
  does and what is required to use it. Defaults to an empty string if not provided.
- the function body, which contains the code that is executed when the function is "called"

> - A `function` may accept zero-or-more parameters.

## Calling a function

To use a function, we "call" it.

In earlier chapters we called several functions such as `print`, here we will clarify the syntax.

To call an object, you refer to it by name and add a pair of parenthesis.

For example,

```python
# tests/test_examples/test_functions.py

{{  #include ../../tests/test_examples/test_functions.py:1:5 }}
  {{  #include ../../tests/test_examples/test_functions.py:6:14 }}
```

When calling a function, you can also specify which parameters the arguments fill. this is known
as `keyword parameters`

For example, using the same function as above:

```python
# tests/test_examples/test_functions.py
...

{{  #include ../../tests/test_examples/test_functions.py:16:20 }}

```

> keyword arguments can be presented out of order, but MUST only come after all positional arguments.
>  - the caller can also only present one argument for a given parameter

# Something less contrived

Math functions aside, show me a function that isn't better off copy/pasted into the callsite!
Sure. Remember that `get_valid_input` while loop presented in the [with for loop](loops/while.md)
chapter? Here is the same piece of code in function form!

```python
{{  #include ../../uci_bootcamp_2021/examples/while_loops.py:8:27 }}
```