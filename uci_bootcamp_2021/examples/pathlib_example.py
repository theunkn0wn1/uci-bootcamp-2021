"""
uci_bootcamp_2021/examples/pathlib_example.py
Examples on how to use imports in python
"""

# Brings the module `pathlib` into scope.
import pathlib


# define a function called `main`, which contains the example code.
def main():
    # Create a pythonic pointer to the data file ./data/us-graph-2015-02.csv
    # <repository_root>/data/us-graph-2015-02.csv
    target = pathlib.Path() / "data" / "us-graph-2015-02.csv"

    # read the lines out of the data file
    lines = target.read_text().splitlines()
    # emit the first line of the data
    print(lines[0])

    # build a list of lists containing each individual cell of the CSV; the hard way.
    table = []
    for line in lines:
        table.append(line.split(','))

    return lines


if __name__ == "__main__":
    main()
