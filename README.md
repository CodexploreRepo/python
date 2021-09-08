# Python
ISSS622 - Python Programming and Data Analysis

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Operators](#1-operators)
- [2. Functions](#2-functions)
  - [2.1. Argument Types](#21-argument-types)
  - [2.2. Variable Scopes](#22-variable-scopes)


# 1. Operators
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
- There are 2 types of Variable: `Local` and `Global` variable
  - `Global` variable 

  ```Python
  y = 'global'
  def test():
      global y
      print(y)
  test()    #will print 'global'
  print(y)  #will print 'global'
  ```
