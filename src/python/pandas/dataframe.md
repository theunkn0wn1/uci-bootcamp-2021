# Pandas and the dataframe

Data is often *labeled*, and often data scientists work with multiple streams of data at the same time.

Pandas is a library that handles series of labeled - tabular - data. It often the core library used to
import data from common formats such as `.csv`, `.tsv`, and proprietary formats such as from Microsoft
Excel to enable programatic processing. The core datatype that Pandas provides for this is
the [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

For this and following slides, we will be using download speed data provided by Netflix back in 2015.
For convenience, the dataset is provided in this repository as `data/us-graph-2015-02.csv`

> "The Netflix ISP Speed Index." 27 06 2018. *Netflix.* csv. 27 06 2018
> \<https://ispspeedindex.netflix.com/country/us\>

## A cursory glance at the raw data

```csv
{{ #include ../../../data/us-graph-2015-02.csv }}
```

- This data is table of numerical values, but its intended for a machine to consume.
- This data isn't exactly human-readable.
- A visual inspection confirms this appears to be a comma-seperated-values file, which
  pandas [has a method for parsing](https://pandas.pydata.org/pandas-docs/version/0.23.1/generated/pandas.read_csv.html#pandas.read_csv)

## loading the data into pandas

```python
{{  # include ../../../uci_bootcamp_2021/examples/pandas_example.py:6:20 }}
```

The DF at this state looks like

```
                2012-11-01  2012-12-01  ...  2015-01-01  2015-02-01
Provider                                ...                        
Comcast               2.17        2.10  ...        3.28        3.36
Cox                   2.07        2.00  ...        3.32        3.38
AT&T - U-verse        1.94        1.92  ...        3.03        3.11
Verizon - FiOS        2.19        2.10  ...        3.43        3.53
AT&T - DSL            1.42        1.41  ...        2.13        2.20
[5 rows x 28 columns]
```

> For the full analysis, please see `notebooks/Netflix.ipynb`

# Further reading

This presentation is how I typically use pandas in a nutshell. For further reading please consult
Pandas's [user guide](https://pandas.pydata.org/docs/user_guide/10min.html): 