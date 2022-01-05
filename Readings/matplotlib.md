# Matplotlib

# Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
- [2. Concepts](#2-concepts)
  - [2.1. Figure](#21-figure) 
  - [2.2. Axes](#22-axes)
- [3. Common Plots](#3-common-plots)
- [4. Box Plot](#4-box-plot)

# 1. Introduction
- Matplotlib is a python library to create data visualisations.
- Pyplot module within matplotlib provides a MATLAB-like interface.
- It creates figures and axes to achieve the desired plot.

<img width="700" alt="Screenshot 2022-01-05 at 10 57 19" src="https://user-images.githubusercontent.com/64508435/148158464-a9affe81-07f0-47d5-9749-32b113e33530.png">

# 2. Concepts
- Figure: It may contain one or multiple axes (plots).
- Axes: Known as plots. It contains two (2D) or three (3D) axis objects.
- Axis: Lines with numbers.
<p align="center"><img width="600" alt="Screenshot 2022-01-05 at 11 01 49" src="https://user-images.githubusercontent.com/64508435/148158790-e54b15a9-6b1d-4a61-bd23-e9fe2ca4cf46.png">
</p>


## 2.1. Figure
- Figure object is the overall window where everything is drawn.
- When run `plt.show()`, python will create a default **figure** if there’s no
existing one.
- The default figure only contains one **axes** and the user is unable to call the axes.

```Python
import matplotlib.pyplot as plt 
fig = plt.figure() #optional 
plt.show()
```

## 2.2. Axes
### 2.2.1. Create axes one by one
- Create axes with `add_subplot`
```Python
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)# (n_rows, n_cols, index)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.set(title = 'Axes 1')
ax2.set(title = 'Axes 2')
ax3.set(title = 'Axes 3')
ax4.set(title = 'Axes 4')

fig.tight_layout() #to ensure no overlaps
plt.show()
```

#### 2.2.2. Create all axes at one time

```Python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes[0,0].set(title = 'Axes 1')
axes[0,1].set(title = 'Axes 2')
axes[1,0].set(title = 'Axes 3')
axes[1,1].set(title = 'Axes 4')
plt.show()

#OR

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
ax1.set(title = 'Scatter')
ax2.set(title = 'Line')
ax3.set(title = 'Bar')
ax4.set(title = 'Bar with Artists')
plt.show()
```
<p align="center">
<img width="628" alt="Screenshot 2022-01-05 at 11 18 34" src="https://user-images.githubusercontent.com/64508435/148159947-2ac329bf-c57b-43e0-a3e6-66b2da89f8de.png"></p>


# 3. Common Plots
- Scatter
- Line
- Bar
- Histogram

```Python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), sharex='all', sharey='all') #sharex='all', sharey='all' to share same axis x, y
ax1.set(title = 'Scatter')
ax2.set(title = 'Line')
ax3.set(title = 'Bar')
ax4.set(title = 'Bar with Artists')

ax1.scatter(x,y, marker="+", color="red")
ax2.plot(x,y,marker='*', linestyle='dashed', color="black")
ax3.bar(x,y, edgecolor='black', color='lightblue')

bars = ax4.bar(x,y, color='lightblue')
for bar, height in zip(bars, y):
    if height < 0:
        bar.set(color = 'salmon') #To change the color of each bar based on Height values

plt.show();
```

<p align="center"><img width="600" alt="Screenshot 2022-01-05 at 11 01 49" src="https://user-images.githubusercontent.com/64508435/148159540-64fd2d54-7de1-4feb-9884-ce62ad7db115.png">
</p>

[(Back to top)](#table-of-contents)

# 4. Box Plot
- A boxplot is a standardized way of displaying the distribution of data as below:
    - **whis (whisker)**: `whis = 1.5`, by default. 
  - **“minimum”**: `Q3 + whis*IQR`
  - **first quartile (Q1/25th Percentile)**: the middle number between the smallest number (not the “minimum”) and the median of the dataset.
  - **median**: middle value of the dataset (i.e: half of the numbers in the dataset below the median, half of the numbers in the dataset above the median)
  - **interquartile range (IQR)**: `Q3-Q1` 25th to the 75th percentile.
  - **third quartile (Q3/75th Percentile)**: the middle value between the median and the highest value (not the “maximum”) of the dataset.
  - **“maximum”**: `Q3 + whis*IQR`
- It can tell you about your outliers and what their values are.
  - **outliers**: `those points > (Q3 + whis * IQR) = "maximum" ` or `those points < (Q1 – whis * IQR) = “minimum”`
- It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed.

<img width="697" alt="Screenshot 2022-01-05 at 16 31 07" src="https://user-images.githubusercontent.com/64508435/148194512-75ae6a8c-fdfb-47c7-a811-abca95165adc.png">



[(Back to top)](#table-of-contents)
