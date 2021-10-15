# Pandas

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
  - [1.1. Series](#11-series) 
  - [1.2. DataFrame](#12-dataframe)
    - [1.2.1. Column View](#121-column-view)  
    - [1.2.2. Row View](#122-row-view)
    - [1.2.3. Data Selection](#123-data-selection)



# 1. Introduction
- **2 fundamental data structures** in Pandas: `Series` and `DataFrame`

## 1.1. Series
- One dimensional array-like: `pd.Series(data, index=index)`
- 2 attributes: `data` and `index`
  - **data**: List, Numpy Array, Scalar, Dictionary (keys to be index, values to be values)
  - **Index**: can be non-sequential, duplicates, non-numbers

```Python
# Creating a series with values: [0.1 0.2 0.3] and index: RangeIndex(start=0, stop=3, step=1)
# List
data = pd.Series([0.1, 0.2, 0.3])
0    0.1
1    0.2
2    0.3
dtype: float64

# NumPy array
print(pd.Series(np.array([11,8,3,1])))

# Scalar
print(pd.Series(100)) print(pd.Series(100, index=range(3)))
0    100
1    100
2    100
dtype: int64
```

```Python
# Index Example
val = np.arange(0, 5)
ind = val * 2 # non-sequential index
data = pd.Series(val, index=ind)

0    0
2    1
4    2
6    3
8    4
dtype: int32

ind = [3, 9, 1, 10, 3] #duplicate index
data = pd.Series(val, index=ind) 

ind = ['a', 'b', 'c', 'd', 'e'] #non-number index
data = pd.Series(val, index=ind)
```
## 1.2. DataFrame
- Two-dimensional: a **row index** and a **column index**
- Each column is a pandas `Series`
- “holes” in Series are filled with `NaN` missing value
<p align="center"><img width="400" alt="Screenshot 2021-10-15 at 13 27 03" src="https://user-images.githubusercontent.com/64508435/137436780-4a9f1620-e1b9-4859-8fc9-c6cae411c562.png"></p>

```Python
years = [2000, 2001, 2002, 2003, 2004]
population = {'area_1': [1.1, 1.2, 1.5, 1.7, 2.0],
              'area_2': [0.4, 0.5, 0.7, 0.6, 0.7]}

df = pd.DataFrame(population, index = years)
```
<p align="center"><img width="145" alt="Screenshot 2021-10-15 at 13 30 18" src="https://user-images.githubusercontent.com/64508435/137437024-172ce012-4710-4391-bb3b-6c9937b78503.png"></p>

### 1.2.1. Column View
- **Column Index**: df.columns
- **Column Access**:
  - *Single* column: `df[col_name]` or `df.col_name` (no space in col_name)
  - *Multiple* columns: **column names in a list** `df[[col_name1, col_name2, ...]]`
- **Column Addition**: `df[new_col] = seq` where seq can be List/ or Pandas Series

### 1.2.2. Row View
- **Row Index**: df.index
- **Row Access with .iloc**:
  - `.iloc` indexer: integer position-based
    - `df.iloc[row_num]`
    - `df.iloc[[row_nums]]` select multiple rows
    - `df.iloc[start_row_num:end_row_num]` not including the end_row_num
- **Row Access with .loc**:
  - `.loc` indexer: label-based, which means that you have to specify rows and columns based on their row and column labels.
  - Note: *different from iloc, end index are included, not excluded*
    - `df.loc[row_num]`
    - `df.loc[[row_nums]]` select multiple rows
    - `df.loc[start_row_num:end_row_num]` including the end_row_num

### 1.2.3. Data Selection



[(Back to top)](#table-of-contents)