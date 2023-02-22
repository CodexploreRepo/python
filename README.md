# Python

Python Programming and Data Analysis

# Table of contents

- [Table of contents](#table-of-contents)
- [0. Common Syntax](./docs/common_syntax.md)
- [1. Basics](#1-basics)
  - [1.1. Naming Convention](#11-naming-convention)
  - [1.2 Operators](#12-operators)
  - [1.3. Iterables & Iterators](#13-iterables-and-iterators)
  - [1.4. Zip & Enumerate](#14-zip-and-enumerate)
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
  - [5.4. Magic Methods](#54-magic-methods)
- [6. Regular Expression](#6-regular-expression)
  - [6.0. Regex Summary](#60-regex-summary)
  - [6.1. What is Regex](#61-what-is-regex)
  - [6.2. Search for a pattern](#62-search-for-a-pattern)
  - [6.3. Metacharacters](#63-metacharacters)
  - [6.4. Grouping Constructs](#64-grouping-constructs)
  - [6.5. Flags](#65-flags)
  - [6.6. Module-Level re Methods](#66-module-level-re-methods)
  - [6.7. Look ahead & Look behind](#67-look-ahead-and-look-behind)
- [7. Numpy](./docs/numpy.md)
- [8. Pandas](./docs/pandas.md)
- [9. Matplotlib](./docs/matplotlib.md)

# 1. Basics

## 1.1. Naming Convention

<p align="center"><img height="650" alt="Screenshot 2021-09-08 at 22 32 46" src="https://user-images.githubusercontent.com/64508435/132529262-a62cdade-2b8a-42ad-8b79-06dae10deed6.png"></p>

## 1.2. Operators

- **4 Bascis Data Types**: String, Integer, Float and Boolean
- **Logical Variable**: `not`, `and`, `or`

| Operator | Name           | Description                                        |
| -------- | -------------- | -------------------------------------------------- |
| `a / b`  | True division  | Quotient of `a` and `b`                            |
| `a // b` | Floor division | Quotient of `a` and `b`, removing fractional parts |
| `a % b`  | Modulus        | Integer remainder after division of `a` by `b`     |
| `a ** b` | Exponentiation | `a` raised to the power of `b`                     |

- **Membership Operators**: `in` and `not in`
- **Identify Operators**: `is` and `is not` to identify if 2 variables are same class

```Python
x =5
type(x) is int #True
```

## 1.3. Iterables and Iterators

- **iterable**: types of iterables
  - list/tuple/str/dict
  - zip/enumerate/range/reversed
- **iterator**: An iterable can be passed to the built-in function `iter()`, which returns some object called **iterator**

```Python
it = iter([4, 3, 2, 1])
print(next(it))#4
print(next(it))#3
```

<p align="center"><img height="150" alt="Screenshot 2021-09-08 at 22 32 46" src="https://user-images.githubusercontent.com/64508435/134283766-31d814a5-ac4d-4ab9-b2f2-c29e81ad737b.png"></p>

## 1.4. Zip and Enumerate

- `zip()`: to zip 2 lists together
- `enumerate()`: to return both item & index corresponding to that item in the list

```Python
>>> integers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> floats = [4.0, 5.0, 6.0]
>>> zipped = zip(integers, letters, floats)  # Three input iterables
>>> list(zipped)
[(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]
```

```Python
l1 = ['h', 'e', 'l', 'l', 'o']
for idx, item in enumerate(l1):
    print(idx,item)

0 h
1 e
2 l
3 l
4 o
```

[(Back to top)](#table-of-contents)

# 2. Functions

## 2.1. Argument Types

- **2.1.1. Positional Arguments**
- **2.1.2. Keyword Arguments**
- **2.1.3. Default Arguments**
- **2.1.4. Variable-Length Arguments**

  1. `*args` (Non-Keyword Arguments): extra arguments can be tacked on to your current formal parameters (including zero extra arguments)
  2. `**kwargs` (Keyword Arguments) : dictionary that maps each keyword to the value that we pass alongside it

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
  - **argument_list** (same as argument list in functions): `x,y, *arg, **kwargs`
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
- **Map** syntax : `map(function, iterable)` applies a given function to each item of the given iterable
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

random.random() #return random number between [0.0 and 1.0)
>>> 0.35553263284394376
random.uniform(0, 10) #return a random floating point number N from uniform distribution such that a <= N <= b, where a=lower_end, b=higher_end
>>> 3.58
random.randint(0, 10) #generate a random integer between two endpoints in Python
>>> 7
random.gauss(mu, sigma) #return a random floating point number with gaussian distribution.

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

- **Immutable** (when values are changed, a new object will be created): integers, strings, and tuples
- **Mutable** (values can be changed after creation): lists, dictionaries, and sets
<p align="center"><img width="802" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/132581542-e3c2e12a-efe1-4c64-9750-e39d2091b36d.png"></p>

[(Back to top)](#table-of-contents)

## 5.2. Class

### 5.2.1. Class Definition

- **Class** is a "blue-print" for creating **Object**
  - For example: Cars may not be exactly same, but the structures are same.
  <p align="center"><img height="300" alt="Screenshot 2021-09-09 at 04 38 24" src="https://user-images.githubusercontent.com/64508435/132582020-fffa406a-96ac-4848-aab1-ec55b61a4394.png"></p>

### 5.2.2. Class Syntax

- **Class attribute**: `Student.num_of_stu` is an attribute for the whole class, _cannot_ use self.num_of_stu
- **Init method**: `__init__` & using self as the first argument
- **Class Method**: at least one argument – self and can be include other method argument like `birth_year`

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

    def full_name(self, birth_year): #Method, we have at least one argument – self & birth_year
      return self.first + ' ' + self.last + ' was born in '  + birth_year

print(Student.num_of_stu) #0
stu_1 = Student('Ryan','Tan')
stu_1.full_name('1995') # "Ryan Tan was born in 1995"
print(Student.num_of_stu) #1
```

## 5.3. Inheritance

- For example, Create `Representative` class based on the `Student` class
- `super()`: to inherite all the attributes in parent class & Initiate more information than parent class
- **Override**: to override the method of parent class

```Python
class Rep(Student):
    def __init__(self, first, last, cat):
      #parent class Student handles existing arguments
      super().__init__(first, last)
      #new information
      self.cat = cat
    def full_name(self): #override the full_name method of parent
      return self.cat + ' representative: ' + super().full_name()
```

[(Back to top)](#table-of-contents)

## 5.4. Magic Methods

- Magic methods in Python are the special methods that start and end with the double underscores \_\_
- Built-in classes in Python define many magic methods. Use the `dir()` function to see the number of magic methods inherited by a class.
  ```Python
  >>> dir(int)
  ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', ...]
  ```
- Magic methods are most **frequently used to define behaviors of predefined operators** in Python

  - For example: `__str__()` method is executed when we want to `print` an object in a printable format. We can override the functionality of the `__str__()` method. As an instance:

    ```Python
    class Human:
        def __init__(self, id, name, addresses=[], maps={}):
            self.id = id
            self.name = name
            self.addresses = addresses
            self.maps = maps

        def __str__(self):
            return f'Id {self.id}: {self.name}'
    human = Human(1, 'Quan Nguyen', ['Address1', 'Address1'], {'London':2, 'UK':3})
    print(human) #Id 1: Quan Nguyen
    ```

[(Back to top)](#table-of-contents)

# 6. Regular Expression

## 6.0. Regex Summary

- **Character class**: `[]` specify a set of characters to match
- **Metacharacters**: `\w` [a-zA-Z0-9_], `\W` [^a-za-z0-9_], `\d`, `\D`, `\s` (white-space), `\S` (non white-space), `.` match anything except \n
- `\` to remove special meaning of the metacharacter. For example: [\.] means match "." dot in the text, not mean match anything
- **Anchors**: `^`, `$`, `\b` to get grid of \n at beginning & end of text:
  - `^` beginning of text line, `$` end of text line: use `re.M` to match the beginning ^ /end $ pattern in multiple lines
  - `\b` word boundary match until last word character `[a-zA-Z0-9_]`
- **Quantifiers**: `*` zero or more , `?` zero or one, `+` one or more, `{m}` m repetitions, `{m, n}` any number of repetitions from m to n, inclusive: to repeating literal/metacharacter/group/backreference
- **Group**: to keep certain part out of the entire match, or match a repeat with backref
- **Backreference**: Numbered groups: `\1`, `\2`, `\3` numbering: from out to in, from left to right
- [**Look ahead & Look behind**](#67-look-ahead-and-look-behind)

## 6.1. What is Regex

- **Regex**: is a tiny programming language used for data manipulation
- **re** module: is a Python module containing _re engine_ and providing the regular expression functionality

<p align="center"><img height="150" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/134284925-92986820-ff2a-4e1e-a7be-6803a4656dab.png"></p>

## 6.2. Search for a pattern

- To search for a pattern, there are 2 steps:
  - **Step 1**: Compile the pattern
  - **Step 2**: Perform the search
  <p align="center"><img height="250" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/134285694-4c822104-ae2e-4eb2-9d4b-6ca380295c62.png"></p>

### 6.2.1. Compile the pattern

- `re.compile()` function compiles a pattern so that the re engine can perform the search.

```Python
pat = re.compile(r'abc')
print(pat)
print(type(pat))

re.compile('abc')
<class 're.Pattern'>
```

### 6.2.2. Perform the search

#### 6.2.2.1. Match()

- `match()`: match the pattern **from the beginning**.

```Python
mat_abc1 = pat.match('ABC,ABc,AbC,abc')
mat_abc2 = pat.match('abc,ABc,AbC,abc')
print(mat_abc1) #None because pattern 'abc' not appear at the beginning
print(mat_abc2) #<re.Match object; span=(0, 3), match='abc'>
```

#### 6.2.2.2. Search()

- `search()`: match the pattern in **any position** in the text and returns the match in `re.Match` class.
- BUT it **only returns the first match**

```Python
sear_abc1 = pat.search('ABC,ABc,AbC,abc')
sear_abc2 = pat.search('abc,ABc,AbC,abc')

print(sear_abc1) #<re.Match object; span=(12, 15), match='abc'>
print(sear_abc2) #<re.Match object; span=(0, 3), match='abc'>
print(type(sear_abc1))#<class 're.Match'>
```

#### 6.2.2.3. Findall()

- `findall()` method: finds all the matched strings and return them in a list.

```Python
find_abc1 = pat.findall('ABC,ABc,AbC,abc')
find_abc2 = pat.findall('abc,ABc,AbC,abc')

print(find_abc1) #['abc']
print(find_abc2) #['abc', 'abc']
```

#### 6.2.2.4. FindIter()

- The `findall()` method returns all the matched strings in a list.
- `finditer()`: returns an iterator that lazily splits matches one at a time.

```Python
finditer_abc = pat.finditer('abc,ABc,AbC,abc')

print(finditer_abc) #<callable_iterator object at 0x7ff650853040>

for m in finditer_abc:
    #<re.Match object; span=(12, 15), match='abc'>
    #<re.Match object; span=(0, 3), match='abc'>
    print(m)
```

## 6.3. Metacharacters

The metacharacters can be categorized into several types as below:

- `. ^ $ * + ? { } [ ] \ | ( )`

- `"["` and `"]"`
- _Type 1_ `. [] - ^ \d \D \w \W \s \S`: Metacharacters that match a single character:

  - `.` **Dot**: match any single character except the newline **\n** character
    ```Python
    p = re.compile(r'.at')
    m = p.findall('cat bat\n sat cap') #['cat', 'bat', 'sat']
    ```
  - `[]` **character class**: specify a set of characters to match
    - Metacharacters lose their special meaning inside character class.
    ```Python
    p = re.compile(r'[abcABC]')
    m = p.findall('abcABC') #['a', 'b', 'c', 'A', 'B', 'C']
    ```
  - `-` **hyphen**: specify a range of characters to match

    - If you want to match a literal hyphen, put it in the beginning or the end inside [], for ex: `[-a-e]` or `[a-e-]`

    ```Python
    p = re.compile(r'[a-z0-9]')
    m = p.findall('d0A3z6P') #['d', '0', '3', 'z', '6']

    p = re.compile(r'[-a-e]') # or [a-e-] if you want to match a hyphen -
    m = p.findall('e-a-s-y, easy') #['e', '-', 'a', '-', '-', 'e', 'a']
    ```

  - `^` **caret**: match any character NOT in the character class

    - A caret ^ not at the beginning of a character class, it works as a normal character
    - A caret outside a character class has a different meaning.

    ```Python
    p = re.compile(r'[^0-9a-z]') #Pattern exclude 0-9 and lowecase of a to z
    m = p.findall('1 2 3 Go') #Result: [' ', ' ', ' ', 'G'] &#8594; Only match space + G

    p = re.compile(r'[0-9^a-z]')#if ^ not at the beginning of a character class, it works as a normal character
    m = p.findall('1 2 3 ^Go') #['1', '2', '3', '^', 'o']
    ```

  - `\d` vs `\D` **digits**: \d (numeric digits) \D (non-digit, including \n)
    ```Python
    p = re.compile(r'\d')
    m = p.findall('a1\nA#')   #['1']
    p = re.compile(r'\D')
    m = p.findall('a1\nA#') #['a', '\n', 'A', '#']
    ```
  - `\w` vs `\W` **word characters**: \w (`[a-zA-Z0-9_]`) \W (`[^a-zA-Z0-9_]`)
    <p align="center"><img height="100" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/134301630-40ca4653-2651-4bd9-8eb5-df0294287fb4.png"></p>

    ```Python
    p = re.compile(r'\w')
    m = p.findall('_#a!E$4-') #['_', 'a', 'E', '4']

    p = re.compile(r'\W')
    m = p.findall('_#a!E$4-') #['#', '!', '$', '-']
    ```

  - `\s` vs `\S` **white space**: \s (white-space) \S (non white-space) match based on whether a character is a whitespace
    <p align="center"><img height="100" alt="Screenshot 2021-09-09 at 04 35 03" src="https://user-images.githubusercontent.com/64508435/134302708-a5bd4be0-265f-4c5b-9acd-a2ea1cfa983e.png"></p>

    ```Python
    text = 'Name\tISSS610\tISSS666\nJoe Jones\tA\tA\n'

    p = re.compile(r'\s')
    m = p.findall(text) #['\t', '\t', '\n', ' ', '\t', '\t', '\n']
    ```

- _Type 2_: Escaping metacharacters: `\` Removes the special meaning of a metacharacter

  ```Python
  p1 = re.compile(r'.')
  p2 = re.compile(r'\.')
  m1 = p1.findall('smu.edu.sg') #['s', 'm', 'u', '.', 'e', 'd', 'u', '.', 's', 'g']
  m2 = p2.findall('smu.edu.sg') #['.', '.']

  p = re.compile(r'\d\\d') #First \d is to match any digit, then second \\d is to match "\d"
  m = p.findall('135\d') #['5\\d'] i.e: 5\d
  ```

- _Type 3_: Anchors: `^` beginning of text, `$` end of text, `\b` word boundary

  - `^` **beginning of text**: We have seen a caret used in a character class. Here the caret is used without a character class.

    - It matches the starting position in the text.
    - In the case of Multiline text, we can add flag `re.MULTILINE` or `re.M` in `re.compile`

    ```Python
    p = re.compile(r'^a[ab]c')
    m = p.findall('''aac\nabc''') #['aac']

    p = re.compile(r'^a[ab]c', re.M) #Add flag re.M to match multiple text
    m = p.findall('''aac\nabc''') #['aac', 'abc']
    ```

  - `$` **end of text**:

    - It matches the ending position in the text
    - Similar to caret, dollar sign matches the ending position but not in each line in multiline text, but this behavior can also be changed with `re.MULTILINE` or `re.M`

    ```Python
    p = re.compile(r'ab.$')
    m = p.findall('abc abd abe abf') #['abf']

    p = re.compile(r'[ab]c$', re.M) #Add flag re.M to match multiple text
    m = p.findall('ac\nbc') #['ac', 'bc']
    ```

  - `\b` **word boundary**: Match based on whether a position is a word boundary

    ```Python
    p = re.compile(r'\b\d\d\b')
    m = p.findall('1 2 3 11 12 13 111 112 113') #['11', '12', '13']

    p = re.compile(r'\b\w\w\b')
    m = p.findall('aa,ab;ac(AA)AB AC') #['aa', 'ab', 'ac', 'AA', 'AB', 'AC']
    ```

- _Type 4_: Quantifiers:

  - `*`: zero or more
  - `?`: zero or one
  - `+`: one or more
  - `{m}`: m repetitions
  - `{m, n}`: any number of repetitions from m to n, inclusive.

  ```Python
  p = re.compile(r'a[ab]*c')
  m = p.findall('a ab ac abc aac aabc aaac ababc') #['ac', 'abc', 'aac', 'aabc', 'aaac', 'ababc']

  p = re.compile(r'a[ab]+c')
  m = p.findall('a ab ac abc aac aabc aaac ababc') #['abc', 'aac', 'aabc', 'aaac', 'ababc']

  p = re.compile(r'a[ab]?c')
  m = p.findall('a ab ac abc aac aabc aaac ababc') #['ac', 'abc', 'aac', 'abc', 'aac', 'abc']

  p = re.compile(r'\d{3}')
  m = p.findall('1 2 3 11 12 13 111 112 113') #['111', '112', '113']

  p = re.compile(r'\d{2,3}')
  m = p.findall('1 2 3 11 12 13 111 112 113') #['11', '12', '13', '111', '112', '113']
  ```

## 6.4. Grouping Constructs

<p align="center"><img width="600" alt="Screenshot 2021-09-23 at 11 08 51" src="https://user-images.githubusercontent.com/64508435/134449409-b15b02e3-d723-48a5-8a87-bb6a427fbaa6.png"></p>

### 6.4.1. Grouped Pattern

- We can group pattern using `()` into sub-patterns

  ```Python
  p = re.compile(r'(\w+): (\d+)') #Sub-patterns are 2 group
  m = p.findall('Course: Grade\nMath: 89\nPhysics: 92\n English: 78') #[('Math', '89'), ('Physics', '92'), ('English', '78')]

  chapters = 'Chapter 12: Numpy\n\
  Chapter 13: Pandas\n\
  Chapter 14: Data Visualzation'
  p = re.compile(r'^Chapter (\d+: .+)', re.M) #['12: Numpy', '13: Pandas', '14: Data Visualzation']
  m = p.findall(chapters)
  ```

### 6.4.2. Alternation

- Match the sub-pattern before or the one after
  ```Python
  p = re.compile(r'(\w+)\.(bat|zip|exe)')
  m = p.findall('game.exe auto.bat text.zip') #[('game', 'exe'), ('auto', 'bat'), ('text', 'zip')]
  ```

### 6.4.3. re.Match.groups() vs re.Match.group()

- `.groups()`: return all matched groups
- `.group()`: allows users to choose different groups by giving the indices of the groups.

  - group(0) returns the whole match.
  - group(1) returns the 1st captured group.
  - group(2, 3, 4) returns the 2nd, 3rd and 4th groups.

    ```Python
    #Ex 1:  re.Match.groups() vs re.Match.group()
    p = re.compile(r'(\w+\.\w+)\s(\w+\.\w+)')
    m = p.search('game.exe auto.bat text.zip')

    print(m.groups()) #('game.exe', 'auto.bat')
    print(m.group(1)) # game.exe

    #Ex 2: re.Match.group()
    pattern = r'(\w+)\W+(\w+)\W+(\w+)\W+(\w)+'
    p = re.compile(pattern)
    m = p.search('one,,,two:three++++++4')
    print(m.group(0)) #one,,,two:three++++++4 (i.e: the whole match)
    print(m.group(1)) #one (i.e: match only group 1)
    print(m.group(2, 3, 4)) #('two', 'three', '4')
    ```

### 6.4.4. Back Reference (\1, \2, \3, ...)

- `'(\w+)-\1'` is different from `'(\w+)-\w+'`
- `'(\w+)-\1'` : when the first group is matched, `\1` match the same literal string in group1
- For example: two patterns both match ‘one-one’, but the one with backreference, `'(\w+)-\1'`, won’t match ‘one-two’.
  ```Python
  # pattern tries to match the type of number that starts with a few digits followed by one digit
  # and then repeats the first few digits.
  p = re.compile(r'((\d+)\d\2)')
  m = p.finditer('1234123, 11311, 123, 54345')
  for string in m:
      print(string.group(1, 2))
      #('1234123', '123') (i.e: 123 - 4 - same as group 2, in this case is 123)
      #('11311', '11')
      #('434', '4')
  ```

## 6.5. Flags

Three common flags that are very useful are:

- `re.MULTILINE` or `re.M` : make “^”/“$” match starting/ending position of each line.
- `re.IGNORECASE` or `re.I`: match letters in a case-insensitive way.
- `re.DOTALL` or `re.S` : make “.” match any character, including newlines \n.

```Python
p1 = re.compile(r'abc')
m1 = p1.findall('abc ABC aBC Abc') #['abc']

p2 = re.compile(r'abc', re.I)
m2 = p2.findall('abc ABC aBC Abc') #['abc', 'ABC', 'aBC', 'Abc'] because re.I means Ignore Case
```

## 6.6. Module-Level re Methods

### 6.6.1. re.match, re.search, re.findall, re.finditer

- Using the module-level methods can skip the step compiling the pattern.

```Python
match = re.match(r'abc', 'abc')
search = re.search(r'abc', 'a abc')
findall = re.findall(r'abc', 'abc abc ab bc a b c')
finditer = re.finditer(r'abc', 'abc abc ab bc a b c')

print(f'match: {match}') #<re.Match object; span=(0, 3), match='abc'>
print(f'search: {search}') #<re.Match object; span=(2, 5), match='abc'>
print(f'findall: {findall}') #findall: ['abc', 'abc']
print(f'finditer: {finditer}') #<callable_iterator object at 0x7fb2e9796a30>
```

### 6.6.2. String-modifying methods

#### Split()

- By default, the `split()` method returns a list of strings broken down, **excluding the matched strings**.
- It is also possible to make split() return the matched strings, simply by using a group to capture the whole pattern.

```Python
p = re.compile(r'\W+')
split = p.split('The~split*method-is%powerful') #['The', 'split', 'method', 'is', 'powerful'], by default

#It is also possible to make split() return the matched strings, simply by using a group to capture the whole pattern.
p = re.compile(r'(\W+)')
split = p.split('The~split*method-is%powerful') #'The', '~', 'split', '*', 'method', '-', 'is', '%', 'powerful']
```

#### Sub(replacement string, text to match the pattern) & Subn()

- `sub()` returns a new string after replacement.
- `subn()` returns a tuple containing the new string and the number of replacements.

```Python
p = re.compile(r'Toko')
sub = p.sub('Tokyo', 'Toko is a large city.') #Tokyo is a large city.
subn = p.subn('Tokyo', 'Toko is Toko') #('Tokyo is Tokyo', 2)
```

## 6.7. Look ahead and Look behind

### 6.7.1. Look ahead (Look Forward)

#### Look ahead positive `(?=)`

- Find expression A where expression B is matching: `A(?=B)`

```Python
p = re.compile(r"\s(\w+(-\w+){1,3}(?=[\s.]))") #(?=[\s.]) match A if B=[\s.] is matching either space or dot.
m = p.findall('''
The man is good-looking and rich.
The eleven-year-old twenty-five-storey building was developed by a famous developer in town.
This art piece is one-of-a-kind.
There is a five-and-one-half-foot-long sign at the outskirt of the town.''')
#[('good-looking', '-looking'), ('eleven-year-old', '-old'), ('twenty-five-storey', '-storey'), ('one-of-a-kind', '-kind')]
```

#### Look ahead negative `(?!)`

- Find expression A where expression B does not follow:`A(?!B)`

### 6.7.2. Look behind (Look Backward)

#### Look behind positive `(?<=)`

- Find expression A where expression B precedes: `(?<=B)A`

#### Look behind negative `(?<!)`

- Find expression A where expression B does not precede: `(?<!B)A`

[(Back to top)](#table-of-contents)
