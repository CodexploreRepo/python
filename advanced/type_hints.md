# Type Hints

## `mypy` Static Type Checker
- `mypy` is a static type checker for Python. It allows us to check our code for common type errors before we actually run anything.

```Python
def main(name: str) -> str:
    return 'Hello ' + name
if __name__=='__main__':
    main('John')
# -------
# mypy program.py
# >> Success: no issues found in 1 source file
```
