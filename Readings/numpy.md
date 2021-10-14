# Numpy

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
    - [1.1. Motivation for Numpy](#11-motivation-for-numpy)
    - [1.2. ndarray](#12-ndarray)
    - [1.3. Indexing & Slicing](#13-indexing-and-slicing)

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


### 1.2.2. ndarray.ndim & ndarray.shape
- `ndarray.ndim`: return number of dimensions
- `ndarray.shape`: return size of each dimension. For 1D array, shape will be `(row, )`.
```Python
print(arr.ndim) #1
print(arr.shape) #(6,0) - For 1D array, each element in the array will be treated as a row, so it will has 6 rows, 0 column

print(arr2d.ndim) #2
print(arr2d.shape) #(2,3) - For 2D array, 2 rows 3 columns
```


[(Back to top)](#table-of-contents)
