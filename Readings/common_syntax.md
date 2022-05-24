# Python Commonly-Used Syntax

# Table of contents
- [Table of contents](#table-of-contents)
- [Python](#python) 
  - [venv](#venv)
  - [I/O](#input-output)
  - [Random Number](#random-number) 
  - [List](#list)
  - [Dict](#dict)
  - [Pathlib](#pathlib)
  - [Utils](#utils)
- [Pandas](#pandas)
  - [Basics](#basics)
  - [`.str`](#str)
  - [Select and Index](#select-and-index)
  - [Concat DataFrame](#concat-dataframe)
  - [Save and Load DataFrame](#save-and-load-dataframe)
  - [`.apply()` and Lambda Function](#apply-and-lambda-function)
- [Numpy](#numpy)
  - [Basics](#basics) 
  - [Vector Arithmetic](#vector-arithmetic)
  - [SciPy Spare and Numpy Dense Matrix](#scipy-spare-and-numpy-dense-matrix)
  - [Stacking Numpy Arrays](#stacking-numpy-arrays)
- [Matplotlib](#matplotlib)
  - [Axis Label](#axis-label)
  - [Save Figure](#save-figure) 
- [Sklearn](#sklearn)
  - [Pre-Processing](#pre-processing)
  - [Model Training](#model-training)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Error Analysis](#error-analysis)

# Python
## Venv
### Create a new virtual environment
Step 1: create a new virtual enviroment `venv`
```
virtualenv venv
```
Step 2: activate the `venv`
```
source venv/bin/activate
```
Step 3: install the dependencies in the *requirements.txt*
```
pip install -r requirements.txt
```
## Input Output
- Write lists of strings into to text file
```Python
sentences = ["Do you know?", "why it so popular.", "The quick brown fox runs over the lazy dog"]
with open("./data/week1_test.txt", "w", encoding="utf-8") as filePtr:
  for sentence in sentences:
    filePtr.write(sentence + "\n")
```
- Read from text file
```Python
with open("./data/week1_test.txt", "r", encoding="utf-8") as filePtr:
  for line in filePtr:
    print(line)
```
## Random Number
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

## List
- `list_a[-100:]` get the last 100 items in the list
- `list_a.extend([1,2,3])` merge 2 lists together (simliar to `list_a + [1,2,3]`)
- `list_a[::-1]` reverse the list

## Dict
### Access a value in Dict vs Key
- `dict_a.get("key_1", 0)` if the key_1 is not exist, then return value 0.
### Sorting a Dict
- Based on values: `dict(sorted(name_diff.items(), key=lambda x: x[1], reverse = True))`
### Default Dict
- Return the default value if the key does not exists
```Python
from collections import defaultdict
 # Function to return a default values for keys that is not present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"]) #1
print(d["b"]) #2
print(d["c"]) #Not Present - Default value when key is not exist
```
- A simplified version of `def_value` using `lambda`
```Python
x = defaultdict(lambda: defaultdict(lambda: 0)) 
# x[key1][sub_key] returns 0 if sub_key does not exist
# x[key1] returns a defaultdict(lambda: 0))
```

[(Back to top)](#table-of-contents)

## Pathlib
```Python
from pathlib import Path
#go back 1 level
#.resolve() as parent is not supported on Windows
main_dir = Path(__file__).resolve().parents[1]
#Same as os.path.join(main_dir, "samples", "templates")
form_dir = main_dir/"samples"/"templates"
```
- `.glob("*.pdf")` to loop through all the files end with ".pdf"
```Python
for file_path in form_dir.glob("*.pdf")
  print(file_path)
```
- ` str(temp_pdf_path.resolve())`: convert the Pathlib to string
- `resolve()` this makes your path absolute and replaces all relative parts with absolute parts, and all symbolic links with physical paths. On case-insensitive file systems, it will also canonicalize the case (file.TXT becomes file.txt).
  - The difference between resolve and absolute is that absolute() does not replace the symbolically linked (symlink) parts of the path, and it never raises `FileNotFoundError`. It does not modify the case either.
  ```Python
  # check beforehand
  if p.exists():
      p = p.resolve()

  # or except afterward
  try:
      p = p.resolve()
  except FileNotFoundError:
      # deal with the missing file here
      pass
  ```
- `.exits()` to check if the file exists
- `.is_dir()`, `.iterdir()`, `.is_file()` check if Path is Dir or File
  ```Python
  input_filepath = Path(input_filepath)
  if input_filepath.is_dir(): #to check if the path is Dir
     for x in input_filepath.iterdir(): #iter the sub-dir
         if x.is_file():
              files_to_process.append(x)
  ```
- `.stem` (get only the file name without extension), `.name` (full name)
  ```Python
  p = Path("/home/user/Downloads/repo/test.txt")
  print(p.stem) #test
  print(p.name) #test.txt
  ```

[(Back to top)](#table-of-contents)

## Utils
### Shallow and Deep Copy
- **Shallow Copy** `copy()`: will **only create a new object for the parent layer**. 
  - It will **NOT** create a new object **for any of the child layer**.
- **Deep Copy** `deepcopy()`: will **create new objects for the parent & child layers**.
```Python
import copy
a = [[0, 1], 2, 3]

#Shallow Copy: will only create a new object for the parent layer.
#it will NOT create a new object for any of the child layer.
b = copy.copy(a)

#only b has 4 appended, not a 
b.append(4) #a: [[0, 1], 2, 3]; b: [[0, 1], 2, 3, 4]
#both a[0][0] and b[0][0] will be updated to 9
b[0][0] = 9 #a: [[9, 1], 2, 3]; b: [[9, 1], 2, 3, 4]


c = copy.deepcopy(a)
c.append(5) #a: [[9, 1], 2, 3], c: [[9, 1], 2, 3, 5]
c[0][0] = 8 #a: [[9, 1], 2, 3], c: [[8, 1], 2, 3, 5]
```

### Google Colab
- Mount the Google Drive to Colab
```Python
from google.colab import drive
drive.mount('/content/drive')
```
-  Linux Command on Google Colab
```Python
!python --version #to check python version
!pip list #to list python modules

!apt-get install python3.8 #get the lastest python version on Colab
!python3.8 -m pip install transformers #to install new packages

#Run Shell Command
!python -c 'print("Hello Word")'
!python ./week1/hello_world.py # run hello_world.py
```
- Hide a code cell by adding `#@title name_of title` in the code cell.
### Pickle
```Python
#Load models:
pickle.dump(model, open(path,"wb"))
#Load models:
pickle.load(open(path,"rb"))
```
### TQDM
- Progress Bar
```Python
from tqdm import tqdm

X_train = []
for row in tqdm(train_df['tokens']):
    model_vector = document_vector(row, sg_w2v_model)
    X_train.append(model_vector)
    
#100%|██████████| 1193/1193 [07:11<00:00,  2.77it/s]
```
[(Back to top)](#table-of-contents)

# Pandas
#### Basics
- `df.set_index("col_name_1", inplace=True)` or `df.set_index(["col_name_1", "col_name_2"], inplace=True)`: to set columns as the index
- `df = pd.read_csv(data_path, index_col="col_name_1")`: to set a column as index when loading data
- `df.reset_index(drop=True)`: to reset the index of the dataframe
```Python
#drop = True, to not retain the old index as a column
df = df.reset_index(drop=True)
```
- `df.sample(n=5, random_state=1)`: randomly select 5 samples from the dataframe
- `df[col].unique().tolist()`: to get List of Unique values in a column
#### `.str`
- **.contains**
  - `df[~df[col].str.contains("Addendum|Endorsement|Payslips")]`: to select rows containing/not containing multiple selected values

#### Select and Index
- Indexing Pandas DF: integer rows, named columns
  - `df.iloc[880, [df.columns.get_loc(c) for c in ['filename','label']]]` 
- Select with Multiple Conditions: 
  - AND: `df.loc[(df.col_1.isnull())&(df.col2 == 'Mr'), 'col3_name']`
  - OR: `df.loc[(df.col_1.isnull())|(df.col2 == 'Mr'), 'col3_name']`
#### Concat DataFrame
- Column Concat: `pd.concat([df_1, df_2], axis= 1, ignore_index=True)`
- Row Concat: `pd.concat([df_1, df_2], axis= 0, ignore_index=True)`
#### Save and Load DataFrame
- Deep copy DataFrame
```Python
train_bkp = train_df.copy(deep=True)
test_bkp = test_df.copy(deep=True)
```
- DataFrame can be stored as pickle files
```Python
#Save DataFrame
df.to_pickle('../data/cleaned_train_v2.pkl')
#Load DataFrame
df = pd.read_pickle('../data/cleaned_test_v2.pkl')
```
#### Apply and Lambda Function
- To modified the data in the col
```Python
num_regex = re.compile(r'[0-9]+')
df["col"].apply(lambda x: len(num_regex.findall(x)))
 
#preprocess_data: is a separate function
df["col"].apply(lambda doc: preprocess_data(doc))  
```
[(Back to top)](#table-of-contents)

# Numpy
## Basics
- `np.unique(array)`: to get the unique values in the array
- **Numpy to List**: `a.tolist() #a is a numpy array`  
- **Numpy's append** numpy arrays: `a1 = [[1], [2], [3]]` and `a2 = [[4], [5]]` &#8594; `[[1], [2], [3], [4], [5]]`
  - `axis` the axis along which values are appended. If axis is not given, both arr and values are flattened before use.
  - `numpy.append(a1, a2, axis = 0)`
- `np.squeeze`: to remove single-dimensional entries from the shape of an array.
  - Shape of input array `a`:  (1, 2, 3)  &#8594; Shape of output array `np.squeeze(a)`:  (2, 3)
## Vector Arithmetic
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

## SciPy Spare and Numpy Dense Matrix
### Convert from SciPy sparse matrix" to a "NumPy matrix"
- For example: `a` is a sparse matrix
  - `a.toarray()` return (numpy.array, **recommended**) a *dense ndarray* representation of this matrix. 
  - `a.todense()` return (numpy.matrix) a *dense matrix* representation of this matrix. 
### Stacking SciPy Spare Matrices
- `scipy.sparse.hstack`: Stack sparse matrices horizontally (column wise)
- `scipy.sparse.vstack`: Stack sparse matrices vertically (row wise)
```Python
from scipy.sparse import coo_matrix, hstack
A = coo_matrix([[1, 2], [3, 4]])
B = coo_matrix([[5], [6]])
# H-Stack Example
hstack([A,B]).toarray()
#array([[1, 2, 5],
#       [3, 4, 6]])

# V-Stack Example
vstack([A, B]).toarray()
#array([[1, 2],
#       [3, 4],
#       [5, 6]])
```
## Stacking Numpy Arrays
- `np.hstack`: Stack arrays in sequence horizontally (column wise).
- `np.vstack`: Stack arrays in sequence vertically (row wise).
  - `np.concatenate(list_of_arrays, axis=0)`
```Python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# H-Stack Example
np.hstack([a,b])
#array([1, 2, 3, 4, 5, 6])

# V-Stack Example
np.vstack([a,b])
#array([[1, 2, 3],
#       [4, 5, 6]])
```

[(Back to top)](#table-of-contents)
# Matplotlib
## Axis Label
- **Label Rotation** in x-axis/y-axis:
  - `plt.xticks(rotation = 90)`:
  - `ax1.tick_params(axis='x', labelrotation=45)`
- **Label Overwritting** in x-axis/y-axis:
```Python
# Get current yticks: An array of the values displayed on the y-axis (150, 175, 200, etc.)
ticks = ax.get_yticks()
# Format those values into strings beginning with dollar sign
new_labels = [f"${int(tick)}" for tick in ticks]
# Set the new labels
ax.set_yticklabels(new_labels)
```
## Save Figure
```Python
fig = plt.figure()
# Any plot in between
fig.savefig(img_path.png)
```

[(Back to top)](#table-of-contents)

# Sklearn
## Pre-processing
### None-value Removal
- `.dropna(subset=['col_name_1'])`: 
- `df[df['col_name_1'].notna()]`: much faster than *.dropna*
### Duplication Removal
- `.duplicated()`: to check any duplicated rows in the DataFrame
- `.drop_duplicates(subset=['col_name_1', 'col_name_2'], keep='last')`: remove duplicates
  - *subset*: specific column(s)
  - *keep* = {‘first’, ‘last’, False} default ‘first’: determines which duplicates (if any) to keep. - first : Drop duplicates except for the first occurrence.
```Python
train_df.duplicated().sum() #check if any duplication

#keeping only the first instance of the duplicate rows 
bool_series = train_df.duplicated(keep='first') 
train_df = train_df[~bool_series]
```
### Label Encoding
- To encode the categorical variables to number
```Python
label_enocoder = sklearn.preprocessing.LabelEncoder()
# Encoding "Target" to number 
y_train = label_enocoder.fit_transform(labeled_train_df['label'].values)
```
- To *inverse transform* from number back to orignal categorical variables' name: 
  - `label_enocoder.inverse_transform(y_test)`
- To get the label & name mapping
```Python
my_tags = list(label_enocoder.classes_)
# my_tags = ['Addendum', 'Endorsement', 'Finance_Report', 'Insurance_Sheet']

# Label & Name mapping
le_name_mapping = dict(zip(label_enocoder.classes_, label_enocoder.transform(label_enocoder.classes_)))
#{'Addendum': 0,
#'Endorsement': 1,
#'Finance_Report': 2,
#'Insurance_Sheet': 3,
```

[(Back to top)](#table-of-contents)
## Model Training
### Baseline Models
- For ex: Classification Problem
```Python
#Define Model
models = [RandomForestClassifier(n_estimators=100, max_depth=5, random_state=2022),
          LinearSVC(),
          MultinomialNB(),
          LogisticRegression(random_state=2022)]

#Define k-fold
cv = 5
kfold = StratifiedKFold(cv, shuffle=True, random_state = 2022)
cv_df = pd.DataFrame(index=range(cv * len(models))) #create a DataFrame with (k-fold * number of models) rows

entries = []
# Loop through models
for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, X_train_vect, y_train, scoring='accuracy', cv=kfold)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))
#List down accuracy per fold for each model  
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

#Plot Base-Line Model Performance
plt.figure(figsize=(6,4))
sns.boxplot(x='model_name', y='accuracy', 
            data=cv_df, 
            color='lightblue', 
            showmeans=True)
plt.title("Boxplot of Base-line Accuracy")
plt.xticks(rotation = 90)
plt.show()
```

<p align="center">
<img src="https://user-images.githubusercontent.com/64508435/160365160-9a25e02a-1246-414d-8460-d4dcaa010981.png" width="350" />
</p>

```Python
#Summary
mean_accuracy = cv_df.groupby('model_name').accuracy.mean()
std_accuracy = cv_df.groupby('model_name').accuracy.std()

acc = pd.concat([mean_accuracy, std_accuracy], axis= 1, ignore_index=True)
acc.columns = ['Mean Accuracy', 'Standard deviation']

# sort by accuracy
acc.sort_values(by=['Mean Accuracy'], axis=0 ,ascending=False, inplace=True)
```
<p align="center">
<img src="https://user-images.githubusercontent.com/64508435/160359420-509c7320-ecba-446a-972b-8a8bfa3bd75b.png" width="400" />
</p>

[(Back to top)](#table-of-contents)

## Evaluation Metrics
### Classification Report
- `target_names`: replace target classes (0,1,2,3,..) with the Label's name in Classification Report 

```Python
# my_tags = ['Addendum', 'Endorsement', 'Finance_Report', 'Insurance_Sheet', 'NDA', 'Payslips', 'Term_Sheet']
# target_names=my_tags
print(classification_report(y_test, y_pred_nb, target_names=my_tags))
```

## Error Analysis
### Classification
- To check if mis-classified instance distribution
  - For ex: to check if how many instances of class "RandomPDFs" being mis-classified as other classes. 
```Python
result_df = pd.DataFrame(zip(y_test, y_pred)), columns=["Label", "Pred"])
result_df = result_df[result_df.Label == "RandomPDFs"]
result_df["Pred"].value_counts()
#Finance_Report     77
#Others              9
#Endorsement         6
```
[(Back to top)](#table-of-contents)
