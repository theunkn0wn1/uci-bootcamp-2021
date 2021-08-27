# The Set

The `set`, AKA a `hashset`, is an **unordered**, resizable, heterogeneous data structure that has the
properties of a [Discrete mathematics Set](http://discrete.openmathbooks.org/dmoi3/sec_intro-sets.html)
.

- All items of a set
  are [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable)
- All items of a set are unique, based on their hash.
- The intersection, union, disjunction, etc can be taken between Sets.
- `Contains` checks against a set are O(1), which can make them quite fast.
- Insertions are idempotent, as all items are unique.

## Declaring a set

Sets are declared using `{}` curly-braces with commas between values

```python
{{  #include ../../../uci_bootcamp_2021/examples/sets.py:0:12 }}
```

> Warning: this syntax very similiar to [`dict`](),
> To declare an **empty** set, you need to call `set()`.
>
> `{}` is interpreted as a dictionary literal!

 ```python
 {{  #include ../../../uci_bootcamp_2021/examples/sets.py:13:21 }}
 ```

# Sets have unique elements

All elements of a set, by definition, are distinct and unique. This property can be quite useful for
reducing duplicate data.

 ```python
 {{  #include ../../../uci_bootcamp_2021/examples/sets.py:22:37 }}
 ```

As stated above, set operations can be done against Python's `set`.

# Union

```python
{{  #include ../../../uci_bootcamp_2021/examples/sets.py:40:49 }}
```

# Intersection

```python
{{  #include ../../../uci_bootcamp_2021/examples/sets.py:50:55 }}
```

# Difference
> Note: the difference between two sets is not associative. A-B != B-A

```python
{{  #include ../../../uci_bootcamp_2021/examples/sets.py:57:65 }}
```

# Further Reading

This is not an exhaustive reference, please consult
the [standard library documentation](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset)
for more information.
