# 2023

### Matplotlib

- Set params:

```Python
plt.rcParams.update({'font.size': 14})
```

### Python General
- `sys.path` is a built-in variable within the sys module. It contains a list of directories that the interpreter will search in for the required module. When a module(a module is a python file) is imported within a Python file, the interpreter first searches for the specified module among its built-in modules. If not found it looks through the list of directories(a directory is a folder that contains related modules) defined by sys.path.
- `assert`: to check if the data is expected (`assert len(x.shape) == 2`) and will raise Exception if not matching.

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
  - Open the Command Palette (`CMD + Shift + P`). Search the “Preferences: Configure Language Specific Settings” and press enter. And search the “Python” and press enter. It will open the “settings.json”.
  ```json
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
  ```
