# Basics Python

## Code Formater

- The [PEP 8 (Python Enhancement Proposal)](www.python.org/dev/peps/pep-0008/) describes best practices for formatting code, and most IDEs and text editors will have tools to help you format your code so that it’s easier to read and find problems.

## Code Linter

- A code linter is a tool that will report problems in your code, such as declaring a variable but never using it.
- Two most popular code linter: [Pylint](www.pylint.org/) and [Flake8](http://flake8.pycqa.org/en/latest/), and both can find errors in your code that the Python interpreter itself will not complain about.
- [Mypy](http://mypy-lang.org/) can use to find problems along with type hints, such as using text when you should be using a number.

## Pip

- Show package information: `pip show -f <pkgname>`
- Upgrade package: `pip install --upgrade <pkgname>`
- Uninstall & install again: `pip install --ignore-installed <pkgname>`

## Python IDLE

- Python can run into 2 modes: Interactive (**Python IDLE**, **IPython**) & Script mode
- The _IDLE_ application (REPL because it’s a Read-Evaluate-Print-Loop) allows you to interact directly with the Python language. Each statement you type is evaluated when you press Enter, and the results are shown in the window.
- The _IPython_ program is yet another “interactive Python” REPL that has many enhancements over IDLE and python3

## Shebang `#!`

- Python programs live in plain text files
- It’s common to put a special comment line in programs like `#!/usr/bin/env python3` these to indicate which language needs to be used to execute the commands in the file.
- Python will ignore the shebang, but the operating systems (like macOS or Windows) will use it to decide which program to use to run the rest of the file.
- Below is the shebang you should add at the beginning of the file

```
#!/usr/bin/env python3
```

- The shebang line tells the operating system to use the `env` program (located at `/usr/bin/env`) to find the **python3** that is specific to the machine on which it’s running.

### Executable Python Program

- So far we’ve been explicitly telling python3 to run our program (`python3 hello.py`), but since we added the shebang, we can execute the program directly and let the OS figure out that it should use python3.
- The first step in doing this is to make our program “executable” using the command `chmod`

```bash
chmod +x hello.py # +x will add an “executable” attribute to the file

#  Now can run the program like
./hello.py
```
