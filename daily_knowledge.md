# 2023
## Day 6
### Numpy
- Stacking columns/rows
  -  `np.column_stack` & `np.row_stack`
  -  `np.hstack` & `np.vstack`
```Python
a = np.array((1,2,3))
b = np.array((2,3,4))
# column stack
np.column_stack((a,b))
# array([[1, 2],
#       [2, 3],
#       [3, 4]])

# row_stack or vstack
np.row_stack((a,b))
np.vstack((a,b))
# array([[1, 2, 3],
#        [2, 3, 4]])

# hstack
np.hstack((a,b))
# array([1, 2, 3, 2, 3, 4])
```
### Holidays package
- Pandas's holiday package: `pandas.tseries.holiday`
- `holidays` package
### Code Refactor
- Instead of `if '.yml' in file_path or '.yaml' in file_path` we can do as follows:
  - Solution: `if any(ext in file_path for ext in ['.yml', '.yaml']` 
## Day 5
### Seaborn
- To get color palatte `color_pal = sns.color_palette()`
#### Pairplot
- Pairplot is to use `scatterplot()` for each pairing of the variables and `histplot()` for the marginal plots along the diagonal
- Customise with `x_var` and `y_var` and `hue`
```Python
sns.pairplot(df.dropna(),
             hue='hour',
             x_vars=['hour','dayofweek',
                     'year','weekofyear'],
             y_vars='PJME_MW',
             height=5,
             plot_kws={'alpha':0.15, 'linewidth':1.5}
            )
plt.suptitle('Power Use MW by Hour, Day of Week, Year and Week of Year')
plt.show()
```

<p align="center"><img height=300 src="https://github.com/CodexploreRepo/python/assets/64508435/75ec4bff-9773-496b-a9fa-dc38549e8938"></p>


### Python
- `yield` keyword is used in the context of defining generator functions.
  - When a generator function is called, it doesn't execute the function immediately.
  - Instead, it returns a generator object that can be used to control the execution of the function.
  - The code inside the generator function is executed only when an item is requested from the generator using the `next()` function or a `for` loop.

```Python
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# using next() to access the code inside
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # StopIteration raised

# using for-loop to iterate through the generator
for value in simple_generator():
    print(value)

```
### Pandas
### Select columns based on Dtype
- Numerical columns: `num_cols = df.select_dtypes(include=np.number).columns.tolist()`
- Categorical columns: `cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()`
### Time-series 
- Convert the datetime index to a datetime col: `df['date'] = df.index.date`
- Slicing using 1 date by including `23:59:59`
```Python
end_train = '1980-01-01 23:59:59'
# including 23:59:59 means
data_train = df.loc[:end_train] # ends at 1980-01-01
data_test  = df.loc[end_train:] # start at 1980-01-02
```
#### `df.query`
- Can set multiple condition: `df.query("make == 'bmw' and model == '1_series')`
- Can query using a list
```Python
holiday_list = ['2021-01-01', '2022-09-02']
df.query('datetime_col in @holiday_list')
```
#### Check & Remove Duplicates
- `df.duplicated()` to check if there are any row duplicate. This will return `True` for the 2nd occurence of the duplicate 
  - `df.duplicated(subset=['col_A','col_B','col_C'])` in case there is no entire row duplciate, we can check duplicates for only subsets of columns
- `df.query("make == 'bmw' and model == '1_series' and year == 2013 and price == 31500")` using query to identify & view the duplicated rows
- Remove the duplicates
  - `.reset_index(drop=True)` to reset the index after dropping the duplicates
  - `.copy()` to make the deep copy of the dataframe
```Python
df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])] \
    .reset_index(drop=True).copy() 
```
### Matplotlib

- You can set matplotlib object to `ax` variable
  - You also can continue to plot on the same graph with `ax` variable
```Python
# case 1: get ax from the plot via pandas dataframe
ax = df['year'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top 10 Years Coasters Introduced')

# case 1.1: also can continue to plot on the same graph with ax variable
df.query('year < 2023').plot(style='.', ax=ax)

ax.set_xlabel('year')
ax.set_ylabel('count')

# case 2: get ax from the plot via seaborn
ax = sns.countplot(data=df, x='year')
ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(), rotation=90, ha='center')
```
- Rotate the xticks label
```Python
# rotate via plt
plt.xticks(rotation=90)

# rotate via ax
ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(), rotation=45, ha='right')
```
## Day 4
### Numpy
- Numpy 's `np.nan` vs Python 's `None` object
  - In Numpy, a `np.nan` value is a native floating-point type array.
    - When you try to do some arithmetic operations will `np.nan`, the result will always be `np.nan`.
    - Fortunately, Numpy provides some special aggregation methods that can ignore the existence of `np.nan` value such as `np.nansum(arr)`
  - `None` is a Python Object called **NoneType**
    - Pandas automatically converts the `None` to a `np.nan` value.
    - If you try to aggregate over this array, you will get an error because of the NoneType.
### Pandas
- `df.loc[:, "col"] = df["col"].map(mapping)` re-assign the updated value to originial column without any error
- `pd.set_option('max_columns', 200)` to view all the columns in the df when `df.head()`
#### `groupby`
-  create a new column by using the transform `function` of pandas along with `groupby`
```Python
# Group by col_1, count by col_2, and then count
df.groupby(["col_1"])["col_2"].count() 

# Group by col_1, count by col_2, and then count
# Create a new column with count values by using transform
df.groupby(["col_1"])["col_2"].transform("count")
```
### Python
- `IPython` debug: when executing `main.py` script in the terminal, we still can insert **ipython** checkpoint at the line we want to debug
  - `from IPython import embed; embed()`
- Avoid circular imports 
  ```
  # __init__.py of utils folder
  from .base_logger import *
  from .data_loader import *

  def load_yaml()

  # data_loader.py
  from utils import load_yaml # this will cause circular import
  ```
  - Solution: DO NOT `from .data_loader import *` if a data_loader refer to any functions in `utils.__init__.py`
### `.env`
- Installation: `pip install python-dotenv==1.0.0`
- Config file stores in `.env` file
```shell
HUGGINGFACEHUB_API_TOKEN="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"
```
- Load environmental variables
```Python
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("../config/.env") 
# load_dotenv(find_dotenv()) # find_dotenv() is to find the .env 
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ... # insert your API_TOKEN here
```

## Day 3
### Notebook 
- Surpass the warning
```Python
import warnings
warnings.filterwarnings('ignore')
```
- Both `!` and `%` allow you to run shell commands from a Jupyter notebook
  - Difference: `!` calls out to a shell (in a new process), while `%` affects the process associated with the notebook
    - `!cd foo`, by itself, has **no lasting effect**, since the process with the changed directory immediately terminates.
    - `%cd foo` changes the current directory of the notebook process, which is a **lasting effect**.
  - Example
  ```Bash
  # in a notebook cell
  !git clone https://github.com/full-stack-deep-learning/fsdl-text-recognizer-2021-labs # ! can use for git clone, pip install
  %cd fsdl-text-recognizer-2021-labs                                                    # % use for cd
  ```

### VScode

- Multiline editing in Visual Studio Code:
  - Mac: `⌥ Opt`+`⌘ Cmd`+`↑/↓`
  - Windows: `Shift`+`Alt`+`↑/↓`

### Matplotlib

#### Figure

- Figure object is the overall window where everything is drawn.

```Python
def draw_smtg():
  fig = plt.figure(figsize=(10,10))
  plt.plot(...)

  return fig #whatever the graphs in fig will be returned
```

### Python

- Logging level: `DEBUG > INFO > WARNING > ERROR > CRITICAL`
  - If set `logging.basicConfig(level=logging.ERROR)` means that only log `ERROR` & `CRITICAL`
- `reload` a module in Jupyter notebook

```Python
from importlib import reload
from abc import module_a
# By doing this, whatever code change in class_xyz will be reflected in the notebook
reload(module_a)
from abc.module_a import class_xyz
```

- `python -m pip install <some-package>`
  - [`-m` flag](https://stackoverflow.com/a/69527909/7973510) makes sure that you are using the pip that's tied to the active Python executable.
- Load pickle file using `joblib`

```Python
model = joblib.load('lgbm_mode.pkl')
```

## Day 2

### Pandas
- `df = pd.read_csv('example.csv',index_col=[0], parse_dates=[0])` to set the col loc=0 as the index, and parsed as date time type
- `to_csv` to prevent `nnamed: 0` column to be appended along with your original df by set `df.to_csv('result.csv', index=False)`
- `.apply` based on the condition of certain columns

```Python
df.loc[:,'C'] = df.apply(lambda row: 'Hi' if row['A'] > 10 and row['B'] < 5 else '')
```

- `df.insert()` Avoid error `Try using .loc[row_indexer,col_indexer] ` when creating the new column in df from an existing df

```Python
# insert(position of the newly_inserted_col in the df, newly_inserted_col's name, newly_inserted_col's value)
data.insert(len(data.columns), 'rolling', data['open'].rolling(5).mean().values)
```

#### Joining Pandas DataFrame

- Experience: before joining (either `concat`, `merge`), need to careful about the _index_ of the dataframes (might need to `.reset_index()`) as apart from the joining condition, pandas also matching the index of each dataframe.

<p align="center"><img height=300 src="https://user-images.githubusercontent.com/64508435/229827362-91a5d973-9e62-4e05-9356-701732e1b9dd.png"><br>Column Concat<br>
<img height=250 src="https://user-images.githubusercontent.com/64508435/229823282-0ea6ebb5-0d21-4ca7-8c96-50d025364fce.png"/><br>
Merge [Inner, Outter (Left, Right)]
</p>

- `concat()` for combining DataFrames across rows or columns
  - **axis** represents the axis that you’ll concatenate along.
    - The default value is **0**, which concatenates **along the index**, or row axis.
    - Alternatively, a value of **1** will concatenate vertically, **along columns**. You can also use the string values "index" or "columns".
  - `ignore_index` defaults to False.
    - If True, then the new combined dataset won’t preserve the original index values in the axis specified in the axis parameter. This lets you have entirely new index values.
- `merge()` for combining data on common columns or indices
  - **how** defaults to `inner`, but other possible options include `outer`, `left`, and `right`
  - `on`; `left_on` and `right_on` specify a column or index that’s present only in the left or right object that you’re merging

```Python
# ------------ pd.concat() examples ------------
reindexed = pd.concat(
     [df1, df2], ignore_index=True, axis=1
)
# ------------ pd.merge() examples -------------
pd.merge(
     df1, df2, how="left", on=["col_A", "col_B"]
)
# if left & right DF has diff joining col names
pd.merge(
     df1, df2, how="left", left_on=["col_A1"], right_on=["col_A2"]
)
```

### Numpy

- Dense & Sparse Matrix Conversion:
  - Sparse &#8594; Dense: `A.toarray()`
- Numpy vs Tensor:
  - TensorFlow seems to look a lot like NumPy. But here’s something NumPy can’t do: retrieve the gradient of any differentiable expression with respect to any of its inputs.
    - Open a `GradientTape` scope, apply some computation to one or several input tensors, and retrieve the gradient of the result with respect to the inputs.
  - A significant difference between NumPy arrays and TensorFlow tensors is that TensorFlow tensors aren’t assignable: they’re constant

```Python
import numpy as np
x = np.ones(shape=(2, 2))
x[0, 0] = 0.

x = tf.ones(shape=(2, 2))
x[0, 0] = 0. # ERROR: fail, as a tensor isn’t assignable.
```

###  `sys.path`

- `sys.path` is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.
- To locate the installation path of the module: `print(module_name.__file__)`
- Python will locate the module based on the path appears first in `sys.path`, so in order to change prioritise the installation packages, we can do as follow:
```Python
import sys
sys.path.insert(0, '/path/to/site-packages') # location of src 
```

### Matplotlib

- Set params: `plt.rcParams.update({'font.size': 14})`
- Set the style of the plot `plt.style.use('fivethirtyeight') # set at the front of the notebook`
  - Other styles: `seaborn-v0_8-darkgrid`
#### Ax 
- Set vertical axis range: `ax.set_ylim([0,1])` or `plt.gca().set_ylim(0,1) #set vertical range to [0-1]`
- Set horizontal axis range: 
#### Subplots

- Enable subplots share the same axis with `sharex` or `sharey`: `plt.subplots(nrows=3, sharey=True)`
- `fig.tight_layout(pad=2)` function of matplotlib allows to adhust the gap between subplots
  - `pad` parameter to specify gap size

### Python

- `assert`: to check if the data is expected (`assert len(x.shape) == 2`) and will raise Exception if not matching.
- `iter()`: return an iterator for the given a list, set, tuple or object with `__next__()` method.

```Python
phones = ['apple', 'samsung', 'oneplus']
phones_iter = iter(phones)
print(next(phones_iter))
```

- `os.environ[variable]=value` a mapping object that represents the user’s environmental variables.
- `sys.path` is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.
- `random` module
  - Randomly select an item in a list: `random.randint(0, len_x)`
  - Randomly select subset of items in a list:
  ```Python
  # Method 1
  indices_permutation = random.permutation(len(x))
  dataset[indices_permutation][:10]
  # Method 2: select 10 out of the dataset
  indices_permutation = random.sample(range(len(trainset)), 10)
  dataset[indices_permutation]
  ```
  - Normal distribution with mean 0 and standard deviation 1: `np.random.normal(size=(3,1), loc=0., scale=1.)`
  - Uniform distribution between 0 and 1: ` np.random.uniform(size=(3, 1), low=0., high=1.)`

## Day 1

### VS Code

#### VS Code Shortcuts

- `CMD + Shift + P` Command Palette
- `CMD + P` Quickly open files

#### Auto Venv Activation

```json
# in .vscode settings.json
 "python.terminal.activateEnvironment": true
```

## Code Formatter & Linting
- The main coding standard for Python is PEP8 (Python Enhancement Proposal 8)
  - **Linters** such as `flake8` and `pylint` highlight places where your code doesn’t conform with PEP8.
  - **Automatic formatters** such as `black` that will update your code automatically to conform with coding standards.
  - **Type Checker** `mypy` is a static type checker for Python. Type checkers help ensure that you're using variables and functions in your code correctly. With mypy, add type hints (PEP 484) to your Python programs, and mypy will warn you when you use those types incorrectly.
### Setup inside VS Code
- How to install `flack8`:
  - Step 1: Install `black` in virtual environment: `pip install flake8`
  - Step 2: Open the Command Palette (`CMD + Shift + P`) &#8594; Search the “Python: Select Linter” and press enter. Select the “flake8”
- How to install `black`:
  - Step 1: Install `black` in virtual environment: `pip install black`
  - Step 2: Open the Command Palette (`CMD + Shift + P`) &#8594; “Preferences &#8594; Settings”
    - Search “format on save” and check the checkbox
    - Search “python formatting provider” and select the `black`.
  - NOTE: can run black seperately `black -l 80 --preview src/youtube_statistics.py`
- How to install `isort`:
  - Open the Command Palette (`CMD + Shift + P`). Search the “Preferences: Open User Settings (JSON)” and press enter. It will open the “settings.json” and add the follow code into that:
  ```json
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
  ```
### Setup pre-commit using `git hooks`
This is to ensure the code formatter, linting is running before the commit
- install requirements-dev dependencies

```sh
# requirements-dev.txt
flake8
black
mypy
coverage
```

- add `hooksPath` into git config core: `git config --local core.hooksPath .git/hooks/`
- `pre-commit` file inside `.git/hooks/`
  ```sh
  # content inside pre-commit file
  echo "Running lint.sh before commit"
  bash lint.sh
  echo "Linting completed"
  ```
  - make pre-commit file executable via `chmod +x .git/hooks//pre-commit`
- Define the content in `lint.sh`

  ```sh
  # content inside lint.sh
    linting_path="."
    echo "-------------Formatter with black-----------------"
    black $linting_path --line-length=88

    echo "-------------Linting with flake8-----------------"
    flake8 $linting_path --max-line-length=88 --ignore=E203,W503,E231,E266,E722

    echo "-------------Type checking with mypy-----------------"
    mypy $linting_path  --ignore-missing-imports
  ```
### Setup pre-commit using `pre-commit` package
- [Reading](https://medium.com/@anton-k./how-to-set-up-pre-commit-hooks-with-python-2b512290436)
