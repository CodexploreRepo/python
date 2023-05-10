# 2023

## Day 3

### Notebook Env

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

- `to_csv` to prevent `nnamed: 0` column to be appended along with your original df by set `df.to_csv(, index=False)`
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

### Python General

- `sys.path` is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.

### Matplotlib

- Set params: `plt.rcParams.update({'font.size': 14})`
- Set vertical axis range: `ax.set_ylim([0,1])` or `plt.gca().set_ylim(0,1) #set vertical range to [0-1]`

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

- `CMD + Shift + P`: Command Palette
- `CMD + P`: Quickly open files

#### Auto Venv Activation

```json
# in .vscode settings.json
 "python.terminal.activateEnvironment": true
```

#### Code Formatter

- The main coding standard for Python is PEP8 (Python Enhancement Proposal 8)
  - **Linters** such as `flake8` and `pylint` highlight places where your code doesn’t conform with PEP8.
  - **Automatic formatters** such as `black` that will update your code automatically to conform with coding standards.
- How to install `flack8`:
  - Step 1: Install `black` in virtual environment: `pip install flake8`
  - Step 2: Open the Command Palette (`CMD + Shift + P`) &#8594; Search the “Python: Select Linter” and press enter. Select the “flake8”
- How to install `black`:
  - Step 1: Install `black` in virtual environment: `pip install black`
  - Step 2: Open the Command Palette (`CMD + Shift + P`) &#8594; “Preferences &#8594; Settings”
    - Search “format on save” and check the checkbox
    - Search “python formatting provider” and select the `black`.
- How to install `isort`:
  - Open the Command Palette (`CMD + Shift + P`). Search the “Preferences: Open User Settings (JSON)” and press enter. It will open the “settings.json” and add the follow code into that:
  ```json
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
  ```
