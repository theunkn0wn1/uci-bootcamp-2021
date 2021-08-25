# The first program

The common first step in most programming languages is to render the phrase `hello, world!` to the
standard output, so let's do that!

Many compiled languages require creating source files before a single line of code can be written. This
isn't strictly the case for Python, which comes with something called a `REPL`.
> REPL: Read, Execute, Print, Loop.

This REPL basically acts as a shell, allowing the user to execute small amounts of code without having
to first write an entire source file.

To start, open a terminal on your OS and type `python3`.

```bash
~ ⌚ 12:45:35
$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 


```

This drops you into the Python REPL, where you can type python code and see the results.

As promised, lets say hello to that world!

```python
>>> print("Hello, world!")
Hello, world!
>>> 
```

## Unpacking

To better understand what is done, let's unpack the above line of code:

- `print` is builtin function, which accepts one `argument`, and renders that argument it to the
  standard output.

- `"Hello, world!"` is a `string literal`.
    - A "string" in Computer Science is text, a collection of characters.
- `print("hello world")` emits the string `"Hello, World" to the standard output.

More on functions [later](functions.md).