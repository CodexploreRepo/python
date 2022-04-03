# Python Commonly-Used Syntax

# Table of contents
- [Table of contents](#table-of-contents)
- [Python](#python) 
  - [List](#list)
  - [Dict](#dict)
  - [Utils](#utils)
- [Pandas](#pandas)
- [Numpy](#numpy)
  - [Basics](#basics) 
  - [SciPy Spare and Numpy Dense Matrix](#sciPy-spare-and-numpy-dense-matrix)
  - [Stacking Numpy Arrays](#stacking-numpy-arrays)
- [Matplotlib](#matplotlib)
- [Sklearn](#sklearn)
  - [Pre-Processing](#pre-processing)
  - [Model Training](#model-training)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Error Analysis](#error-analysis)
# Python
## List
- `list_a[-100:]` get the last 100 items in the list

## Dict
### Sorting a Dict
- Based on values: `dict(sorted(name_diff.items(), key=lambda x: x[1], reverse = True))`

## Utils
### Pickle
```Python
#Load models:
pickle.dump(model, open(path,"wb"))
#Load models:
pickle.load(open(path,"rb"))
```
[(Back to top)](#table-of-contents)

# Pandas
- `df.reset_index(drop=True)`: to reset the index of the dataframe
```Python
#drop = True, to not retain the old index as a column
df = df.reset_index(drop=True)
```
- `df.sample(n=5, random_state=1)`: randomly select 5 samples from the dataframe
#### Concat DataFrame
- Column Concat: `pd.concat([df_1, df_2], axis= 1, ignore_index=True)`
#### Save & Load DataFrame
- DataFrame can be stored as Pickle files
```Python
#Save DataFrame
df.to_pickle('../data/cleaned_train_v2.pkl')
#Load DataFrame
df.pd.read_pickle('../data/cleaned_test_v2.pkl')
```
#### `.apply()` and Lambda Function
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
- **Numpy to List**: `a.tolist() #a is a numpy array`  
- **Numpy's append** numpy arrays: `a1 = [[1], [2], [3]]` and `a2 = [[4], [5]]` &#8594; `[[1], [2], [3], [4], [5]]`
  - `axis` the axis along which values are appended. If axis is not given, both arr and values are flattened before use.
  - `numpy.append(a1, a2, axis = 0)`
- `np.squeeze'
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
- `plt.xticks(rotation = 90)`: rotate the label in x-axis
-
[(Back to top)](#table-of-contents)

# Sklearn
## Pre-processing
### Duplication Removal
- `.duplicated()`: to check any duplicated rows in the DataFrame
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
