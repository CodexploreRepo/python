# 2023
## Day 3
### Python
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

### Matplotlib
- Set params:
```Python
plt.rcParams.update({'font.size': 14})
```

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
  - Randomly select subset of items in a list: `indices_permutation = random.permutation(len(x)); x[indices_permutation][:10]`
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
