# Pandas

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
  - [1.1. Series](#11-series) 
  - [1.2. DataFrame](#12-dataframe)
    - [1.2.1. Column View](#121-column-view)  
    - [1.2.2. Row View](#122-row-view)
    - [1.2.3. Data Selection](#123-data-selection)
    - [1.2.4. Filter](#124-filter)
    - [1.2.5. Index Manipulation](#125-index-manipulation)
- [2. Updating Rows and Columns](#2-updating-rows-and-columns)
- [3. apply() Function](#3-apply-function)
  - [3.1. DataFrame.Series.apply()](#31-series-apply)
  - [3.2. DataFrame.apply()](#32-dataframe-apply)
- [4. Add or Remove Row Column and DataFrame](#4-add-or-remove-row-column-and-dataframe)
  - [4.1. Concating a DataFrame to Another](#41-concating-a-dataframe-to-another)
  - [4.2. Removing Columns Or Rows](#42-removing-columns-or-rows)
- [5. Sorting Data](#5-sorting-data)
  - [5.1. Sort by Columns](#51-sort-by-columns)
  - [5.2. Sort by Row Index](#52-sort-by-row-index)
- [6. EDA](#6-eda)

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
#Example of  pd.DataFrame
years = [2000, 2001, 2002, 2003, 2004]
population = {'area_1': [1.1, 1.2, 1.5, 1.7, 2.0],
              'area_2': [0.4, 0.5, 0.7, 0.6, 0.7]}

df = pd.DataFrame(population, index = years)

# Example of set_index() function
marks = { 'Names': ['James', 'Andrew', 'Bob', 'Carlson'],
          'English': [58, 62, 77, 65],
          'Chinese': [55, 32, 64, 80],
          'Math': [61, 70, 81, 54]}

df = pd.DataFrame(marks) 
df.set_index("Names", inplace = True) 

# Example of parameter "columns" function
marks = {'James': [58, 55, 61],
         'Andrew': [62, 32, 70],
         'Bob': [77, 64, 81],
         'Carlson': [65, 80, 54]}

df = pd.DataFrame(marks.values(), 
                  index=marks.keys(),
                  columns=['English', 'Chinese', 'Math'])
      
#         English  Chinese  Math
#James         58       55    61
#Andrew        62       32    70
#Bob           77       64    81
#Carlson       65       80    54
```


### 1.2.1. Column View
- **Column Index**: `df.columns`
- **Column Access**:
  - *Single* column: `df[col_name]` or `df.col_name` (no space in col_name)
  - *Multiple* columns: **column names in a list** `df[[col_name1, col_name2, ...]]`
```Python
# Single-column access
print(df['area_1'])
print(df.area_2)

# Multiple-column access
print(df[['area_1', 'area_2']])
```
- **Column Addition**: `df[new_col] = seq` where seq can be List/ or Pandas Series

### 1.2.2. Row View
- **Row Index**: `df.index`
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
#### Loc and iLoc
- Select a portion of data using `.iloc[rows, cols]` (integer position-based) & `loc[rows, cols]` (label-based)
```Python
#iloc examples
df.iloc[:3, -1] #First 3 rows of the last columns
df.iloc[[0, 2], :3] #row 0th and row 2nd from first 3 cols

#loc examples:
df.loc[[2000, 2001, 2003], :'area_2'] #row 2000, 2001 and 2003 with col 'area_2'
df.loc[2001:2002, 'area_3']
```
### 1.2.4. Filter
Data selection with Filter Mask
- **Filter Mask**: `df[filter mask]`
- **Filter Mask**: `df.loc[filter mask,[columns]]`  columns is OPTIONAL 
- **String**: `df[df["col"].isin([value1, value2, value3])]`
- **String**: `df[df["col"].str.contains(r"value1|value2")]`
```Python
df[(df['age'] >= 10) & (df['height'] >= 10)]

df.loc[df['height'] >= 10, ['age', 'weight']]

#isin
data[data['Crime Code'].isin(['624', '510', '230'])

#.str.contains
df[df["Name"].str.contains("Jonkheer")]['Name']
df[df["Name"].str.contains(r'Tyler|Goodwin')] #.str.contains regex
```

### 1.2.5. Index Manipulation
- columns and index: both index objects
- **immutable**: cannot change part of it
- **replaceable**: replace with completely new index range, or use `set_index(col_name)` to convert a column to row_index

```Python
df.index[0] = 1999 #Error as Index is immutable
df.index = range(len(df)) # len(df) gives the number of rows of DataFrame
df.columns = ['a1', 'a2', 'a3'] #replace the new col indexs

df.set_index('year', inplace = True) #remove the col 'year' and set it as the index of df
```

# 2. Updating Rows and Columns
- **Updating rows**: always use the `loc/iloc` indexer. Otherwise, the change only applies to a copy/view
```Python
#SettingWithCopyWarning: Change only applies to a copy/view, NOT the df itself
df[df['last name'] == 'Smith']['last name'] = 'Anderson' #have to use .loc/.iloc in this case. See below solution
#Solution:
df.loc[df['last name'] == 'Smith', ['last name']] =  'Anderson' #change will be updated accordingly
```
- **Updating columns**: 
  - Assign a sequence to the column, or 
  - `.str` class under Series class provides many utilities.
    - `lower`, `upper`, `title`, `capitalize`
    - `isupper`, `islower`, `isalpha`, `isalnum`
    - `find`, `replace`, `contains`
```Python
df['last name'] = list(df['last name'])[::-1] #Assign a sequence to the column

#Make use of str class under Series class
df['last name'] = df['last name'].str.lower() 
df["Name"].str.contains("Mrs. Martin")
```
[(Back to top)](#table-of-contents)

# 3. Apply Function
## 3.1. Series Apply
- Syntax: `pandas.Series.apply(func)`, dealing with one item in the Series but not the Series itself
- **No parentheses** required when passing the function name

```Python
# .apply(provided function)
df['last name'] = df['last name'].apply(str.title)

# .apply(self-defined function)
def change_Josh(fname):
    return 'Joe' if fname == 'Josh' else fname

df['first name'] = df['first name'].apply(change_Josh)

# .apply(lambda function)
import re
p = re.compile(r"\b(\w+)\.")
df["Title"] = df["Name"].apply(lambda s: p.search(s).group(1)) #Apply regex to split the "Title" out of "Name"
```

## 3.2. DataFrame Apply
- Syntax: `pandas.DataFrame.apply(func)`, apply a function along an axis of the DataFrame.
- Axis parameters: by default, axies = 0 i.e applies to columns
  - 0 or ‘index’: apply function to each column.
  - 1 or ‘columns’: apply function to each row.

```Python
#Given below DataFrame
   A  B
0  4  9
1  4  9
2  4  9
#Apply function np.sqrt to all columnns in df
df.apply(np.sqrt)
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0
#Apply function np.sum to all rows in df
df.apply(np.sum, axis=1)
0    13
1    13
2    13
```
[(Back to top)](#table-of-contents)

# 4. Add or Remove Row Column and DataFrame
## 4.1. Concating a DataFrame to Another
### 4.1.1 Concat DataFrame
- `pd.concat([df1,df2, df3])`
  - **axis = 0 (By Default)**: append next df by row, similar to `append`
  - **axis = 1**: append next df by column
    - `axis=1, join="inner"` Take the union of them all (Default)
    - `axis=1, join="outer"` Take the intersection

```Python
#By default, axis = 0 => Similar to append by row
result = pd.concat([df1, df2, df3])
```
<p align="center"><img width="400" alt="Screenshot 2021-10-15 at 13 27 03" src="https://user-images.githubusercontent.com/64508435/139216000-859a11e1-2b45-4f68-b616-14af4c51f585.png"></p>

```Python
#By default, axis=1 => join="inner" - Union
result = pd.concat([df1, df4], axis=1) 

#join="inner" = Intersect - the second picture below
result = pd.concat([df1, df4], axis=1, join="inner") 
```
<p align="center">
  <img width="500" alt="Screenshot 2021-10-15 at 13 27 03" src="https://user-images.githubusercontent.com/64508435/139216509-c5e13ce9-658b-48fa-b46c-d30116af333c.png">
  <img width="500" alt="Screenshot 2021-10-15 at 13 27 03" src="https://user-images.githubusercontent.com/64508435/139216557-3bcc660a-4c05-42ce-af0e-e643f44903bd.png">
</p>

### 4.1.2. Append DataFrame
- A useful shortcut to concat() are the `append()` instance methods on Series and DataFrame. 
- These methods actually predated concat. They concatenate **along axis=0**, namely the index:
- `df = df.append(df2, ignore_index=True)`: Appending a DataFrame to Another 
  - resulting DataFrame must be assigned to the original or a new df since no inplace parameter to apply the change to the original DataFrame.
  -  **ignore_index=True**: to reset the index
```Python
result = df1.append([df2, df3, ignore_index=True]) #Append multiple dataframes to df1
result = df1.append(df4, sort=False) #Append df1 & df4, since they have different columns, so whatever missing values will be filled with NaN as shown below
```
<p align="center"><img width="400" alt="Screenshot 2021-10-15 at 13 27 03" src="https://user-images.githubusercontent.com/64508435/139180149-7632060a-2e0b-464c-97c9-7c51b230e1ad.png"></p>


## 4.2. Removing Columns Or Rows
- `pandas.Series.drop(index)`
  - remove items with given indices from a Series
- `pandas.DataFrame.drop(index, axis=0, inplace=True)`
  - remove rows or columns from a DataFrame
  - remove columns: axis = 1 or axis = ‘columns’

```Python
# Series
df['gender'].drop([3, 4]) #drop index =3, and =4 of Series 'gender'

# DataFrame
df.drop([3, 4]) #drop row 3 and row 4
df.drop(df[df['gender'] == 'male'].index) #drop the row with the index of column "df[df['gender'] == 'male']"
df.drop('year', axis = 1, inplace=True) #drop the col "year"
```
[(Back to top)](#table-of-contents)

# 5. Sorting Data
## 5.1. Sort by Columns
- `pandas.DataFrame.sort_values(by=col_names, ascending=True, inplace=True)` sort the DataFrame by given columns
```Python
df.sort_values(by='last name')
df.sort_values(by=['last name', 'first name']) #Sort by Two Cols
df.sort_values(by=['last name', 'first name'], ascending=[True, False])
```

## 5.2. Sort by Row Index
- `pandas.DataFrame.sort_index(inplace=True)` sort DataFrame by row index
```Python
df.sort_index(inplace=True)

df["SibSp"].value_counts().sort_index()
```

[(Back to top)](#table-of-contents)

# 6. EDA
## 6.1. Categorical Data
- `.astype('category')` convert the data type
```Python
df["Survived"] = df["Survived"].astype('category')
```
## 6.2. Check Null Values
- NaN or Null values can be counted with the `.isna()` or `.isnull()` method.
```Python
df["Age"].isnull().sum()

df['Age'].isna().sum()
```
## 6.3. Check Unique Values
- Need to understand how many unique values in a column
```Python
df["Ticket"].nunique()
#681
```
## 6.3. Distrbution of Values
- `.value_counts(normalize=True, sort=False)` can help us find out the distribution of the two values in the column.
- `.describe()` to understand the overall distribution
- `.quantile(np.arange(1,11)*0.1)` function helps to get the quantile information, parameter should be between 0 and 1
- `.plot.hist()` to plot Histogram distribution
```Python
df["Survived"].value_counts()
df["Fare"].describe()

df["Age"].quantile(np.arange(1,11)*0.1) # np.arange(1, 11) gives an np.array containing 1 to 10.
#0.1    14.0
#0.2    19.0 most dense area in the distribution is between 19 to 31
#0.3    22.0
#0.4    25.0
#0.5    28.0
#0.6    31.8
#0.7    36.0
#0.8    41.0
#0.9    50.0
#1.0    80.0

df["Age"].plot.hist() # plot a histogram
```

## 6.4. Multi-Column Analysis
- `df.groupby()` creates groups within a DataFrame by a key, i.e., the dateframe is separated into groups according the values of the key. 
  - `__str__()` doesn’t give you much information as `groupby()` lazy in nature. It doesn’t really do any operations to produce a useful result until you say so.
- Various methods of `.groupby()`:
  - **Meta methods & Properties**: `.get_group(value in each group)`
  - **Aggregation methods**: `.value_counts(normalize=True, sort=False)`
```Python
by_state = df.groupby("state")
# Example of __str__()
print(by_state) #__str__() doesn’t give you much information 
#<pandas.core.groupby.generic.DataFrameGroupBy object at 0x107293278>

# Example of .get_group()
by_state.get_group("PA")
#     last_name first_name   birthday   gender type state               party
# 4       Clymer     George 1739-03-16      M  rep    PA                  NaN
#19       Maclay    William 1737-07-20      M  sen    PA  Anti-Administration
#21       Morris     Robert 1734-01-20      M  sen    PA   Pro-Administration

```


[(Back to top)](#table-of-contents)


