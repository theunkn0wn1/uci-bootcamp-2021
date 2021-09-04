# The `for` loop

Now that we have [containers](python/basic_containers/summary.md), we can present loops.

in essence, the `for` loop allows the programmer to *iterate* (to do some repeated action) over the *items* of an iterable, such as a collection.

Let's start with an example.

```python
# uci_bootcamp_2021/examples/for_loops.py

{{  #include ../../../uci_bootcamp_2021/examples/for_loops.py:6:17 }}
```

What happens here is the body of the `for` loop is run multiple times: once for each value in `data`.

Each time it runs, `item` holds a different value, values that come from `data`. In order.

This loop construct works over
any [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable), not
just [`Containers`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container)
.


One common anti-pattern beginner python programmers is to loop over `range`, specifically

```python
# uci_bootcamp_2021/examples/for_loops.py

collection = [2, 1, 32]
# WARNING: Don't do this! antipattern!
for i in range(len(collection)):
    print(i, collection[i])

# 0 2
# 1 1
# 2 32
```

There is, of course, a better way of writing this in python.

```python
# uci_bootcamp_2021/examples/for_loops.py

{{  #include ../../../uci_bootcamp_2021/examples/for_loops.py:21:30 }}
```

For loops are powerful constructs for performing operations against a collection or some other
iterable. They do not require knowing the length of the iterable (if it has one), or any other details
beyond the type of the iterable.
