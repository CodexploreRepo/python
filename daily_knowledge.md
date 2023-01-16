# 2023
## Day 1
### VS Code
#### VS Code Shortcuts
- `CMD + Shift + P`: Command Palette
- `CMD + P`: Quickly open files
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
  - Open the Command Palette  (`CMD + Shift + P`). Search the “Preferences: Configure Language Specific Settings” and press enter. And search the “Python” and press enter. It will open the “settings.json”.   
  ```json
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
  ```
