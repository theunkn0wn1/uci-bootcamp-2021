# Pandas and the dataframe

Data is often *labeled*, and often data scientists work with multiple streams of data at the same time.

Pandas is a library that handles series of labeled - tabular - data. It often the core library used to
import data from common formats such as `.csv`, `.tsv`, and proprietary formats such as from Microsoft
Excel to enable programatic processing. The core datatype that Pandas provides for this is
the [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

For this and following slides, we will be using download speed data provided by Netflix back in 2015.
For convenience, the dataset is provided in this repository as `data/us-graph-2015-02.csv`

> "The Netflix ISP Speed Index." 27 06 2018. *Netflix.* csv. 27 06 2018
>   \<https://ispspeedindex.netflix.com/country/us\>

## A cursory glance at the raw data

```csv
{{ #include ../../../data/us-graph-2015-02.csv }}
```

- This data is table of numerical values, but its intended for a machine to consume.
- This data isn't exactly human-readable.
- A visual inspection confirms this appears to be a comma-seperated-values file, which
  pandas [has a method for parsing]()

## Loading it with pandas

Let's load the data into Python using Pandas!

```python

```