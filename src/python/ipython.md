# IPython - an enhanced interactive Python REPL.

Back in the [Hello-world](hello_world.md) chapter we saw the vanilla python REPL. For what it is, it gets the job
done.

[IPython]() takes the idea of a REPL and adds better features such as tab completion*, multi-line
editing, history, and other really powerful features to the table.

While it is the python kernel backing [Jupyter Notebook](), it can be used standalone without the rest
of the scientific stack installed.

> This particular library is difficult to express in text, for the full experience watch the presentation.

## Launching IPython

IPython, just like the standard Python repl, can be launched from the command line:

```bash
# using the installed alias
ipython3
# Or, to launch ipython witin a specific interpreter
python3 -m IPython
```

## Anatomy of the IPython REPL

After launching IPython, you will be greeted with the following display:

```
~ ⌚ 12:37:04
$ ipython3
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.24.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 

```

`In[n]:` is akin to a *line number*, it is essentialy the `>>>` prompt in the standard REPL.

Let's type some basic python code!

```python
In[1]: x = 7

In[2]: x + 3
Out[2]: 10

In[3]: Out[2] - 4
Out[3]: 6

In[4]:

```

- `In[1]` did't produce an `Out[1]`, this is because assignment operations evaluate to `None`.
- `In[2]` produced an `Out[2]`, which represents the output of `In[2]`.
- `In[3]` uses the value `Out[2]` in a further calculation.
    - `In` and `Out` are special variables IPython provides!

## IPython remembers

IPython keeps a history of inputted commands, which can be retrieved at a later point in time.

This feature can be very useful when the user is many lines down into some knapkin math and needs to
find a calculation done many lines prior.

There are two ways of finding previous inputs:

- Route 1: start typing the first couple characters of the input, then hit up-arrow
- Route 2: Ctrl+r

## IPython allows for editing lines already inserted, but not yet executed.

In the standard python REPL, after a line of code has been submitted, it cannot be changed. For basic
arithmetic, this is not a problem. When writing loops or more complicated expressions, this becomes a
problem.

- For writing any significant length of code, an IDE should be used and not the REPL.

For example:

```
$ python3
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> x = 7
>>> while z > 6:
    ...  # well now i can't go and fix that while statement without starting over again....
KeyboardInterrupt
>>>

```

- IPython allows the user to edit lines 


## Magics
IPython also brings some unique syntax to the table in the form of [magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

One such magic is `%timeit`, which allows the user to benchmark a block of code.
This can be useful when comparing two logically equivalent implementations.