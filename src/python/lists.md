# Python Lists

Python has a number of builtin container types, the most common of which is the `list`.

A `list` is an ordered, resizable, mutable, heterogeneous container.

It is also a precursor to `Numpy`'s `ndarray`. More on that [later.](the_ndarray.md)

- It retains the order of items put into it, unless explicitly sorted
- Additional items can be inserted into, or items removed from, the collection at will.
- The container can be changed at any time (mutability).
- The items don't all have to be the same type (though, in good practice, they should be).

Since it is ordered, it can be used to store time-series data, the lines of a text file, or any other
ordered sequence.

## Declaring a list literal

Lists are denoted by `[]` square brackets, and may contain zero-or-more elements

```python
{{  #include ../../uci_bootcamp_2021/examples/lists.py:0:11}}
```

## Declaring a list from an existing Iterable

Lists can also be declared from
other [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)s.

One common `iterable` is the
builtin [`range`](https://docs.python.org/3/library/functions.html#func-range)).

`range` is a ['Sequence'](https://docs.python.org/3/library/stdtypes.html#typesseq) that produces
integers in the domain `[start, stop)`, every `step` values (default 1).

```python
{{  #include ../../uci_bootcamp_2021/examples/lists.py:12:18 }}
```

## Sorting lists
Lists can also be sorted, provided their elements are sortable.
```python
{{  #include ../../uci_bootcamp_2021/examples/lists.py:20:31 }}
```

## Mutating the contents of a list
The elements of a list can be changed by adding, removing, or by changing existing items.

```python
{{  #include ../../uci_bootcamp_2021/examples/lists.py:34:58 }}
```
