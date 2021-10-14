# Numpy

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
    - [1.1. Motivation for Numpy](#11-motivation-for-numpy)
    - [1.2. ndarray](#12-ndarray)
        - [1.2.1. Creating ndarray From List](#121-creating-ndarray-from-list)
        - [1.2.2. ndarray.ndim and ndarray.shape](#122-ndarray.ndim-and-ndarray.shape)
    - [1.3. Indexing & Slicing](#13-indexing-and-slicing)
    - [1.4. Boolean Masking](#14-boolean-masking)
    - [1.5. Math & Stat Functions](#15-math-and-stat-functions)
- [2. Vector and Matrix Computation](#2-vector-and-matrix-computation)
    - [2.1. Vector Arithmetic](#21-vector-arithmetic) 
    - [2.2. Matrix Shape Manipulation](#22-matrix-shape-manipulation)
    - [2.3. Linear Algebra](#23-linear-algebra)


# 1. Introduction
- `NumPy` is short for **Numerical Python**, using to deal with `ndarray` data structure (array or vector/matrix-based computations)
- Most computational packages providing scientific functionality use NumPy
- Import convention: `import numpy as np`
## 1.1 Motivation for Numpy
- **Add 2 Lists**: The loop structure provides a good mechanism to finish a piece of repetitive work with a reasonable amount of code. However, when number of iterations is large, a loop could take a very long time.

```Python
size = 10000000

# Add 2 lists using For Loop
def add_list(size_of_list):
    l1 = list(range(size_of_list))
    l2 = list(range(size_of_list))
    l = [l1[i] + l2[i] for i in range(size_of_list)]
    return l

# Add 2 list using Numpy 
def add_ndarray(size_of_array):
    l1 = np.arange(size_of_array)
    l2 = np.arange(size_of_array)
    return l1 + l2

%%time
add_list(size) #time: 2.44 s
%%time
add_ndarray(size) #time: 50.9 ms much Numpy faster than using For Loop to add 2 lists
```

## 1.2. ndarray
- NumPy's `ndarray` gives a tool to represent vectors and matrices, represents an *N-dimensional* data.
- `ndarray` takes a block of memory space. NumPy functionalities can operate this entire memory block without a loop structure, making the computation very fast and efficient.
### 1.2.1. Creating ndarray From List
#### 1.2.1.1. Creating ndarray From List using np.array()
- `np.array()` method can  create an array or multi-dimensional array from a list or nested list.
```Python
arr = np.array([0, 1, 1, 2, 3, 5])

arr2d = np.array([[0, 1, 1], 
                  [2, 3, 5]])
```
#### 1.2.1.2. Create commonly used ndarrays
- `np.zeros(shape)` and `np.ones(shape)`: to create all-zero vectors/matrices 
- `np.arange(end)`: equivalence of range() function
- `np.random.randn(d1, d2, d3, ...)`: return a sample (or samples) from the “standard normal” distribution.
    - d1, d2, d3, ... are sizes of each dimension
- `np.random.rand(d1, d2, d3, ...)`: return random samples from a uniform distribution over `[0, 1)`.
- `np.eye(N)`: NxN identity matrix


### 1.2.2. ndarray.ndim and ndarray.shape
- `ndarray.ndim`: return number of dimensions
- `ndarray.shape`: return size of each dimension. For 1D array, shape will be `(row, )`.
```Python
print(arr.ndim) #1
print(arr.shape) #(6,0) - For 1D array, each element in the array will be treated as a row, so it will has 6 rows, 0 column

print(arr2d.ndim) #2
print(arr2d.shape) #(2,3) - For 2D array, 2 rows 3 columns
```

## 1.3. Indexing and Slicing
- **1-dimensional array**: similar to Python list
```Python
arr1d = np.array([2, 3, 4, 5, 6, 7, 9])

print(arr1d[2])     #4
print(arr1d[2:5])   #[4 5 6]
print(arr1d[:-1:2]) #[2 4 6] from begin to the last one (but not include the last one)
```
- **Higher-dimensional array**: use indexing and slicing for each dimension – separate each dimension with comma (,)
```Python
arr2d = np.array([[i+j*4 for i in range(4)] for j in range(4)])

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

print(arr2d[0, :]) #[0 1 2 3]
print(arr2d[0:3, 1:2]) 
[[1]
 [5]
 [9]]
```
## 1.4. Boolean Masking
- Use `&` for “and”, `|` for “or” and `~` for “not” to apply multiple conditions.
```Python
# random data for 4 users in 4x2 matrix
arr_dat = np.random.rand(4, 2)

[[0.45141391 0.19962473]
 [0.51339208 0.35115272]
 [0.43308732 0.32066871]
 [0.82072226 0.45147328]]

# user id from 0 to 3
arr_id = np.arange(4)

# pick data for user id 2
print(arr_dat[arr_id == 2]) #[[0.43308732 0.32066871]]

# pick data for users id 0 and 3
print(arr_dat[(arr_id == 0)|(arr_id == 3)])

[[0.45141391 0.19962473]
 [0.82072226 0.45147328]]
```

## 1.5. Math and Stat Functions
- `sum()` sum
- `mean()` mean value
- `std()` standard deviation
- `min()` minimum
- `max()` maximum
- `cumsum()` cumulative sum
- `cumprod()` cumulative product

```Python
arr = np.arange(16)
print(arr) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(arr.sum())             #120
print(arr.mean(), arr.std()) #7.5 4.6097722286464435
print(arr.min(), arr.max())  #0 15

print(arr.cumsum())  #[  0   1   3   6  10  15  21  28  36  45  55  66  78  91 105 120]
print(arr.cumprod()) #[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
```

[(Back to top)](#table-of-contents)

# 2. Vector and Matrix Computation
## 2.1. Vector Arithmetic
- Arithmetic operations include: `+, -, *, /, //, **, %`
- Arithmetic operations with scalars propagate the scalar argument to each element.
- Comparisons between arrays of the same size yield Boolean arrays.

```Python
arr1 = np.arange(5)
arr2 = np.array(range(5, 0, -1))
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

#arithmetic operations with scalars propagate the scalar argument to each element
print(arr1 + 1)
print(arr1 * 2)
print(1 / arr2)

#comparisons between arrays of the same size
print(arr1 > arr2) #[False False False  True  True]
```

## 2.2. Matrix Shape Manipulation
- `reshape()` method can be used to change the shape of the matrix.
- Use `-1` to imply the size of the other dimension
```Python
arr1 = np.arange(9)
print(arr1, arr1.shape) #[0 1 2 3 4 5 6 7 8] (9,)

mat1 = arr1.reshape(3, 3)

[[0 1 2]
 [3 4 5]
 [6 7 8]] (3, 3)

mat2 = arr1.reshape(3, -1) #use -1 to imply the size of the other dimension.
[[0 1 2]
 [3 4 5]
 [6 7 8]] (3, 3) 
```

## 2.3. Linear Algebra
- `m.T` to get the transpose of a Matrix m
- Matrix Multiplication (Dot Product): `np.dot(m1, m2)`; `m1.dot(m2)`; `m1 @ m2`
– `diag` diagonal elements
– `trace` sum of diagonal elements 
- `det` determinant
