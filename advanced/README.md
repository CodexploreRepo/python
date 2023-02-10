# Advanced Python

## Data Class

Dataclasses, as the name clearly suggests, are classes that are meant to hold data. The motivation behind this module is that we sometimes define classes that only act as data containers and when we do that, we spend a consequent amount of time writing boilerplate code with tons of arguments, an ugly `__init__` method and many overridden functions.
- Type annotation for each attribute. Although this doesn’t enforce type validation, it helps your text editor provide better linting
- dataclass decorator is actually a code generator that automatically adds other methods under the hood: `__init__` , `__eq__` and `__repr__` methods: these methods are responsible for setting the attribute values, testing for equality and representing objects in a nice string format.
```Python
class Person():
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

# dataclass help to remove ugly __init__ method
from dataclasses import dataclass
@dataclass
class Person:
     first_name: str
     last_name: str
     age: int
     job: str
```
