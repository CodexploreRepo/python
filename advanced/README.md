# Advanced Python

## Topics
- [Type Hints](./type_hints.md)

## Class

### Encapsulation

**Encapsulation** describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data

- The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

#### Access Modifiers

**Access modifiers**: Python doesn't have any mechanism that effectively restricts access to any instance variable or method. Python prescribes a convention of prefixing the name of the variable/method with a single (`_`) or double underscore (`__`) to emulate the behavior of protected and private access specifiers.

1. **Public**
2. **Protected**: to add a prefix `_` (single underscore) to it
   - Protected members of a class are accessible from within the class and are also available to its sub-classes. No other environment is permitted access to it.
   - Although the protected variable can be accessed out of the class as well as in the derived class (modified too in derived class), it is customary(convention not a rule) to not access the protected out the class body.
3. **Private**:
   - The double underscore `__` prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an `AttributeError`
   - **Name mangling**: Every member with a double underscore will be changed to `_object._<class_name>__<private_attribute>`. So, it can still be accessed from outside the class, but the practice should be refrained.

## Data Modeling & Validation
- Common Package:  Attrs, Pydantic, or Python Data Classes
   - `Pydantic` is a Python library for data modeling/parsing that has efficient error handling and a custom validation mechanism.
### Python Data Classes

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

## Test-driven development

- The basic idea is that we write tests even before we write code. The tests define what it means to say that our program works “correctly.”
- Test templates:
  - The first test in every exercise checks whether the expected program exists.
  - The second test checks that the program will print a help message if we ask for help.
  - After that, your program will be run with various inputs and options.

## Virtual Environment
### Virtual Env Creation & Activation

- Step 1: `python3 -m venv venv` for initialising the virtual environment
- Step 2: Activating the virtual environment
   - Linux or MacOS `source venv/bin/activate` 
   - Window `venv/venv\Scripts\activate.bat` 

### Dependency Installation

The following commands shall be ran **after activating the virtual environment**.

- `pip install --upgrade pip` for upgrading the pip
- `pip install -r requirements.txt` for the functional dependencies
- `pip install -r requirements-dev.txt` for the development dependencies. (should include `pre-commit` module)
