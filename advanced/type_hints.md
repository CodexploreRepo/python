# Type Hints
## Common Types
```Python
from typing import List, Dict, Tuple
def square_func(arr: List[float]) -> List[float]:
    return [x ** 2 for x in arr]
print(square_func([1, 2, 3])) # 1, 4, 9
```
### `Union`
```Python
from typing import Union
# cache_dir variable either type str or Path
def filename_to_url(filename: str, cache_dir: Union[str, Path] = None) -> Tuple[str, str]:
    pass

```
### `Optional`
```Python
from typing import Optional

Params = dict[str, dict[str, float]]
Descriptions = dict[str, str]

def foo(x: Params) -> Optional[Descriptions]:
    pass
```
### `Callable`
- `Callable` represents something that can be called (e.g. a function) that takes input arguments and returns an output type:
```Python
from typing import Callable
# func varibale is Callable that takes two integer arguments and returns an float
def apply_func(a: int, b: int, func: Callable[[int, int], float]) -> int:
    return func(a, b)

def divide_func(a: int, b: int) -> float:
    return a/b

apply_func(1,2, divide_func)
```
## `mypy` Static Type Checker
- `mypy` is a static type checker for Python. It allows us to check our code for common type errors before we actually run anything.
    - Installation: `pip install mypy`
```Python
def main(name: str) -> str:
    return 'Hello ' + name
if __name__=='__main__':
    main('John')
# -------
# mypy program.py
# >> Success: no issues found in 1 source file
```
