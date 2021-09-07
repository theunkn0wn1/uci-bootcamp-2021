# Pathlib

[Pathlib](https://docs.python.org/3/library/pathlib.html) is a standard-library component that improves
python's cross-platform compatability.

- Different Operating Systems have different ways of describing filesystem paths
- Pathlib abstracts these differences away, allowing for code that behaves the same way regardless of
  OS.

For example:

- On Windows, the "My Documents" folder exists at `C:/users/{user}/Documents`
- On Linux, the equivalent path would be `~/Documents` which typically expands
  to `/home/{user}/Documents`.
- With pathlib, we can refer to this platform-specific directory using [`pathlib.Path.home`](https://docs.python.org/3.8/library/pathlib.html#pathlib.Path.home):

```py
from pathlib import Path

# Path.home refers to the user's home directory
documents = Path.home() / "Documents"
```

> Note that directories and files are accessible by "dividing" an existing `pathlib.Path` object.
>  - By doing it this way, filesystem and os-specific path quirks are abstracted away.

Here is a more complete example, which will be built-upon in the following chapters:

```python
# uci_bootcamp_2021/examples/pathlib_example.py

{{  #include ../../uci_bootcamp_2021/examples/pathlib_example.py:6:20}}
```

This example creates a `Path` to `data/us-graph-2015-02.csv`, which is one of the example datasets
provided in this presentation's repository.

`Path` objects have many methods on them, including `read_text`, which can be used to read the text out of the file without having to explicitly open it.
