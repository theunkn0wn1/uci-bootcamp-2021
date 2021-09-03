# Import this

Now that we have covered [modules](modules.md) and [packages](packages.md), we can finally talk
about `libraries` and how to `import` them.

So what is this `import` you speak so highly of?

In python, the `import` keyword allows us to bring names into scope from another `module` or `package`.

Here is an example using the standard-library [Pathlib](https://docs.python.org/3/library/pathlib.html)
module:

```python
{{  #include ../../uci_bootcamp_2021/examples/pathlib_example.py}}
```

# Libraries

The organization of code into *modules*, which are organized into *packages* forms the backbones of
what we call `Libraries`. Libraries are *packages* that share a common goal: such as providing
filesystem abstractions like `Pathlib` does, or focus on plotting scientific data like `matplotlib`
does.

The ability to `import` code written somewhere else by potentially other people is what forms the
foundation for Python's various communities and the language's wide range of applications.

In the next section, we will cover some of the more important libraries as it relates to scientific
computing, plus some tools that will make writing maintainable Python easier.