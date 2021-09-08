# Python
ISSS622 - Python Programming and Data Analysis

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Basics](#1-basics)
  - [1.1. Naming Convention](#11-naming-convention)
  - [1.2 Operators](#12-operators)
- [2. Functions](#2-functions)
  - [2.1. Argument Types](#21-argument-types)
  - [2.2. Variable Scopes](#22-variable-scopes)
- [3. Lambda Expressions](#3-lambda-expressions)
  - [3.1. Sorted](#31-sorted)
  - [3.2. Filter and Map](#32-filter-and-map) 
- [4. Module](#4-module)

# 1. Basics
## 1.1. Naming Convention
![Screenshot 2021-09-08 at 22 31 36](https://user-images.githubusercontent.com/64508435/132529021-bbdfe6e6-a3f9-4910-9cef-9dc42c5729db.png)

## 1.2. Operators
* **4 Bascis Data Types**: String, Integer, Float and Boolean
* **Logical Variable**: `not`, `and`, `or`

| Operator     | Name           | Description                                            |
|--------------|----------------|--------------------------------------------------------|
| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
* **Membership Operators**: `in` and `not in`
* **Identify Operators**: `is` and `is not` to identify if 2 variables are same class
```Python
x =5
type(x) is int #True
```

[(Back to top)](#table-of-contents)

# 2. Functions
## 2.1. Argument Types 
- **2.1.1. Positional Arguments**
- **2.1.2. Keyword Arguments**
- **2.1.3. Default Arguments**
- **2.1.4. Variable-Length Arguments**
    1) `*args` (Non-Keyword Arguments): extra arguments can be tacked on to your current formal parameters (including zero extra arguments)
    2) `**kwargs` (Keyword Arguments) : dictionary that maps each keyword to the value that we pass alongside it

    **Example of** `*args` 
    ```Python
    def info(name, *args):
        hobby = []
        for a in args:
            hobby.append(a)
        print(name +"'s hobbies: " + ', '.join(hobby))
    info('Mike')                      #Mike's hobbies:
    info('Mike', 'hiking', 'reading') #Mike's hobbies: hiking, reading
    ```
    **Example of** `**kwargs`
    ```Python
    def info(name, **kwargs):
        hobby = []
        for k, v in kwargs.items():
            hobby.append(k+'-'+v)
        print(name +"'s hobbies: " + ', '.join(hobby))
    info('Mike', first='hiking', second='reading') #Mike's hobbies: first-hiking, second-reading
    ```

[(Back to top)](#table-of-contents)

## 2.2. Variable Scopes
- There are 2 types of Variable: `Local` and `Global` scope
  - `global` variable 

  ```Python
  y = 'global'
  def test(): 
      global y #This to declare y is global scope
      print(y)
  test()    #will print 'global'
  ```
[(Back to top)](#table-of-contents)

# 3. Lambda Expressions
- Syntax: `lambda argument_list: expression`
  - **argument_list**  (same as argument list in functions): `x,y, *arg, **kwargs`
  - **expression** (Output) must be single line

**Example of** `lambda` 
```Python
lambda x, y: x*y          #input: x, y; output: x*y
lambda *args: sum(args).  #input: any number of parameters; output: their summation
lambda x: 1  #input: x; output: 1
```
## 3.1. Sorted
- Syntax: `sorted(iterable, key=None, reverse=False)` sorts the elements in the given iterable by key
```Python
sorted([1, 2, 3, 4, 5], key = lambda x: abs(3 - x))  #[3, 2, 4, 1, 5]
```
## 3.2. Filter and Map
- **Filter** syntax: `filter(function, iterable)` filters the given iterable (list) based on the given function
- **Map** syntax   : `map(function, iterable)` applies a given function to each item of the given iterable
- Note: Both Filter and Map will return **Iterable Object**, so need to use `list()` function to convert to a lsit

**Example of** `filter` and `map` 
```Python
list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5]))  #[1, 3, 5]

list(map(lambda x: x + 1, [1, 2, 3]))                #[2, 3, 4]
```

[(Back to top)](#table-of-contents)

# 4. Module
## 4.1. Random Module
```Python
import random
random.seed(42) #make results reproducible,

random.random() #return random number between 0.0 and 1.0
>>> 0.35553263284394376

random.randint(0, 10) #generate a random integer between two endpoints in Python
>>> 7

items = ['one', 'two', 'three', 'four', 'five']
random.choice(items) #choosing multiple elements from a sequence with replacement (duplicates are possible):
>>> 'four'
random.choices(items, k=2)
>>> ['three', 'three']
random.choices(items, k=3)
>>> ['three', 'five', 'four']


random.shuffle(items) #randomize a sequence in-place
>>> ['four', 'three', 'two', 'one', 'five']

```


[(Back to top)](#table-of-contents)

