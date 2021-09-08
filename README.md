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
- [5. Class](#5-class)
  - [5.1. Object](#51-Object)
    - [5.1.1. Variable Assignment and Aliasing](#511-variable-assignment-and-aliasing) 
    - [5.1.2. Comparison Operators](#512-comparison-operators)
    - [5.1.3. Integer Caching](#513-integer-caching)
    - [5.1.4. Shallow Copy vs Deep Copy](#514-shallow-copy-vs-deep-copy)
    - [5.1.5. Data Mutability](#515-data-mutability)
  - [5.2. Class](#52-class)
  - [5.3. Inheritance](#53-inheritance)
 
# 1. Basics
## 1.1. Naming Convention
<p align="center"><img height="650" alt="Screenshot 2021-09-08 at 22 32 46" src="https://user-images.githubusercontent.com/64508435/132529262-a62cdade-2b8a-42ad-8b79-06dae10deed6.png"></p>

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

# 5. Class
<p align="center"><img height="220" alt="Screenshot 2021-09-08 at 22 38 12" src="https://user-images.githubusercontent.com/64508435/132530282-20979abf-6614-4b20-aa15-a2d977456dd8.png"></p>

## 5.1. Object
### 5.1.1. Variable Assignment and Aliasing
- **Aliasing**: many variables (a,b) refer to the same object list `[1,2]`
<p align="center"><img height="350" alt="Screenshot 2021-09-08 at 22 52 48" src="https://user-images.githubusercontent.com/64508435/132532913-a9ab157c-6978-4e5f-be48-5bdc91f07efc.png"></p>

### 5.1.2. Comparison Operators
- `==`: compares the values of the object
- `is`: compares objects

```Python
a = [1,2]
b = [1,2] 

print(id(a)) #2661200625736 
print(id(b)) #2661202091528

a == b #True
a is b #False
```

### 5.1.3. Integer Caching
- In Python, interpreters will typically cache small integers in the range of -5 to 256. 
- When the Python interpreter is launched, these integer objects will be created and available for later use in the memory.
<p align="center"><img height="200" alt="Screenshot 2021-09-08 at 23 32 57" src="https://user-images.githubusercontent.com/64508435/132539689-99e8ee1f-0009-496d-82ed-e9e9a4a64090.png"></p>

### 5.1.4. Shallow Copy vs Deep Copy
```Python
import copy
a = [[0, 1], 2, 3]
b = copy.copy(a)
c = copy.deepcopy(a)
```

#### Shallow Copy - copy()
- Shallow Copy will **only create a new object for the parent layer**. 
- It will **NOT** create a new object **for any of the child layer**.
<p align="center"><img width="741" alt="Screenshot 2021-09-08 at 23 38 28" src="https://user-images.githubusercontent.com/64508435/132541100-72f775f8-ce2c-4522-8cd1-39a179e74bc3.png"></p>

#### Deep Copy - deepcopy()
- Deep Copy will **create new objects for the parent & child layers**. 
<p align="center"><img width="733" alt="Screenshot 2021-09-08 at 23 45 50" src="https://user-images.githubusercontent.com/64508435/132541770-54c04dab-43be-4439-b93f-98cd6aa61064.png"></p>

### 5.1.5. Data Mutability
• **Immutable**  (values are changed, a new object will be created): integers, strings, and tuples
• **Mutable** (values can be changed after creation): lists, dictionaries, and sets 
<p align="center"><img width="802" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/132581542-e3c2e12a-efe1-4c64-9750-e39d2091b36d.png"></p>

[(Back to top)](#table-of-contents)

## 5.2. Class
### 5.2.1. Class Definition
- **Class** is a "blue-print" for creating **Object**
  - For example: Cars may not be exactly same, but the structures are same. 
<p align="center"><img height="300" alt="Screenshot 2021-09-09 at 04 38 24" src="https://user-images.githubusercontent.com/64508435/132582020-fffa406a-96ac-4848-aab1-ec55b61a4394.png"></p>

### 5.2.2. Class Syntax
- **Class attribute**: `Student.num_of_stu` += 1 is an attribute for the whole class, *cannot* use self.num_of_stu
- **Init method**: `__init__` & using self as the first argument
- **Class Method**: at least one argument – self 

```Python
class Student:
    #Class attribute
    num_of_stu = 0 
    
    #Special init method
    def __init__(self, first, last): #use self as the first argument
      self.first = first
      self.last = last
      self.email = first + '.' + last + '@smu.edu.sg'
      Student.num_of_stu += 1 #attribute for the whole class, cannot use self.num_of_stu
    
    def full_name(self): #Method, we have at least one argument – self 
      return self.first + ' ' + self.last
```

## 5.3. Inheritance
- For example, Create `Representative` class based on the `Student` class
- `super()`: to inherite all the attributes in parent class & Initiate more information than parent class
- **Override**: to override the method of parent class
```Python
class Rep(Student):
    def __init__(self, first, last, cat):
      super().__init__(first, last) #parent class handles existing arguments 
      self.cat = cat #new information
    def full_name(self): #override the full_name method of parent class, Student
      return self.cat + ' representative: ' + self.first + ' ' + self.last 
```

[(Back to top)](#table-of-contents)
