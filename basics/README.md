# Basics Python

## Code Formater

- The [PEP 8 (Python Enhancement Proposal)](www.python.org/dev/peps/pep-0008/) describes best practices for formatting code, and most IDEs and text editors will have tools to help you format your code so that it’s easier to read and find problems.

## Code Linter

- A code linter is a tool that will report problems in your code, such as declaring a variable but never using it.
- Two most popular code linter: [Pylint](www.pylint.org/) and [Flake8](http://flake8.pycqa.org/en/latest/), and both can find errors in your code that the Python interpreter itself will not complain about.
- [Mypy](http://mypy-lang.org/) can use to find problems along with type hints, such as using text when you should be using a number.

## Python IDLE

- Python can run into 2 modes: Interactive (**Python IDLE**, **IPython**) & Script mode
- The _IDLE_ application (REPL because it’s a Read-Evaluate-Print-Loop) allows you to interact directly with the Python language. Each statement you type is evaluated when you press Enter, and the results are shown in the window.
- The _IPython_ program is yet another “interactive Python” REPL that has many enhancements over IDLE and python3

## Pip

- Show package information: `pip show -f <pkgname>`
- Upgrade package: `pip install --upgrade <pkgname>`
- Uninstall & install again: `pip install --ignore-installed <pkgname>`
