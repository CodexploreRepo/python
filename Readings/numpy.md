# Numpy

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
- [1.1. Motivation for Numpy](#11-motivation-for-numpy)

# 1. Introduction
## 1.1 Motivation for Numpy
- [Add 2 Lists] The loop structure provides a good mechanism to finish a piece of repetitive work with a reasonable amount of code.
- However, when number of iterations is large, a loop could take a very long time.

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



[(Back to top)](#table-of-contents)
