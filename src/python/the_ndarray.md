# Numpy and the `ndarray`

When working with large amounts of data, the built-in python datastructures begin to show their
limitations.

- The standard `list` is designed for heterogenous data, meaning it uses memory less efficiently than
  something designed to work with homogenous numerical data.
- Numpy's array structures are optimized for doing mathematics such as linear algebra
- They are the backbone of many SciPy libraries and data structures.

> Note: It is strongly advised to consult [Numpy's official documentation](https://numpy.org/devdocs/user/quickstart.html#array-creation).
> The official docs are very well written, and go into more depth than this presentation.

## Basic operations on `numpy` arrays and their standard-library counterparts

```python
# uci_bootcamp_2021/examples/numpy_example.py

{{  #include ../../uci_bootcamp_2021/examples/numpy_example.py:6:37}}

```