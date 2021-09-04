# Variables

Now that we have the ability to do math, we need a place to store the results.

Immediately `print`ing is convenient for demonstration, but not very useful for programs.

A `variable` is a programming construct that gives programmers a place to store data between
calculations. Variables can be used in the same places literals can within expressions, but also be
assigned to using the `=` operator.

For example:

```python
# uci_bootcamp_2021/examples/basic_variables.py

{{  #include ../../uci_bootcamp_2021/examples/basic_variables.py:6:16}}
```

> Warning: in python`=` is used as the *assignment operator*, while`==` is used as the
> *equality relational operator*. It is a common beginner error mistaking these two operators!

```python
# uci_bootcamp_2021/examples/mistaking_equality_for_assigment.py

{{  #include ../../uci_bootcamp_2021/examples/mistaking_equality_for_assigment.py:10:27 }}
```

Variables can hold any value, and be of any type. In fact, a variable may be re-assigned after it is
declared, even if the types don't match!

```python
# uci_bootcamp_2021/examples/basic_variables.py

{{  #include ../../uci_bootcamp_2021/examples/basic_variables.py:18:}}
```

This can be considered one of Python's strengths: Python is a Dynamically Typed language. One of the
major benefits of being dynamically typed is not having to give too much thought to the types a program
requires, and how to obtain them programmatically.

In the context of Data Science, this is a massive boost as it greatly reduces the cognative load on the
programmer. Allowing the focus on more important things such as ensuring their maths are correct, and
manipulating the data into the format required to satisfy the project's constraints.
> Dynamic Typing's strength will become more apparent once we start processing data in the [second half of this presentation]()