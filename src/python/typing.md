# Types

Computers frequently handle different kinds of data.

similar to how there are different *types* of fruits, and different *models* of automobiles, there are
different *types* of data that computers process.

## Noteworthy types

| type | description | example |
 -------| ---------| ------- 
| `str` | a string of text. In modern Python all strings are [`unicode`](https://en.wikipedia.org/wiki/Unicode) | `"I like pizza"`
| `bytes` | representation of an arbitrary stream of bytes. Frequently returned from low-level communication library calls. | `b'\xde\xad\xbe\xef'` |
| `int` | Integers, may be positive or negative. In modern python, they may be of arbitrary size. | `42` |
| `float` | Decimal numbers, represented as [floating point](https://www.eng.auburn.edu/~nelsovp/courses/elec5200_6200/ELEC5200_6200%20Chapter%203%20Float.pdf) values | `0.75` |
| `None` | The lack of a value; roughly comparable to `NULL` in the C-like languages. | `None` |
| `bool` | Boolean values. Something that is either `True` or `False`. | `True`, `False` |
| `list` | Ordered collection of heterogeneous data. see [lists](basic_containers/lists.md)
| `dict` | Key-value pairs of heterogeneous. see [dict](basic_containers/lists.md)
| `set` | unordered collection of heterogeneous data. see [sets](basic_containers/sets.md)


## Type annotations and how python uses types