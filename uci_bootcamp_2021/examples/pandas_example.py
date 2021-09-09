# README: read the notebooks/Netflix.ipynb for better context.
# this file is provided as a non-jupyter version of that notebook, and lacks
# accompanying commentary.


import pathlib

import pandas as pd

# Create a pythonic pointer to the data file ./data/us-graph-2015-02.csv
# <repository_root>/data/us-graph-2015-02.csv
target = pathlib.Path() / "data" / "us-graph-2015-02.csv"

# load the data using pandas.
df = pd.read_csv(
    # the first positional argument is the path to the dataset
    target,
    # here we specify that the first column will be used as the index
    index_col=0
)

# The dataset has trailing whitespace in the index,
# so here we remove that whitespace to make the dataset more intuitive to work with.
df = df.rename(lambda key: key.strip())

# Here we transform the columns, which are dates in the <month>-<shorthand year> format into datetime objects,
# as plotting timeseries is special-cased in pandas and desirable.
df.columns = pd.to_datetime(df.columns, format="%b-%y")

# plot the data, which returns a reference to the plot
ax = df.plot()
# remove the legand from the plotted axis, to make the data slightly easier to read.
ax.get_legend().remove()

df.T.plot(title="Average Netflix download speeds by ISP", ylabel="Download speed (Mbps)",
          figsize=(8, 8))
