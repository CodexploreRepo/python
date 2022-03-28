# Python Commonly-Used Syntax

# Table of contents
- [Table of contents](#table-of-contents)
- [Python](#python)
  - [List](#list)
- [Pandas](#pandas)
- [Numpy](#numpy)
- [Matplotlib](#matplotlib)
- [Sklearn](#sklearn)
  - [Pre-Processing](#pre-processing)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Error Analysis](#error-analysis)
# Python
## List
- `list_a[-100:]` get the last 100 items in the list

[(Back to top)](#table-of-contents)

# Pandas
- `.reset_index(drop=True)`: to reset the index of the dataframe
```Python
#drop = True, to not retain the old index as a column
df = df.reset_index(drop=True)
```
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
# Numpy
# Matplotlib
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
# my_tags = ['Addendum', 'Endorsement', 'Finance_Report', 'Insurance_Sheet', 'NDA', 'Payslips', 'Term_Sheet']

# Label & Name mapping
le_name_mapping = dict(zip(label_enocoder.classes_, label_enocoder.transform(label_enocoder.classes_)))
#{'Addendum': 0,
#'Endorsement': 1,
#'Finance_Report': 2,
#'Insurance_Sheet': 3,
#'NDA': 4,
#'Payslips': 5,
#'Term_Sheet': 6}
```
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
result_df = pd.DataFrame(zip(label_enocoder.inverse_transform(y_test), label_enocoder.inverse_transform(y_pred)), columns=["Label", "Pred"])
result_df = result_df[result_df.Label == "RandomPDFs"]
result_df["Pred"].value_counts()
#Finance_Report     77
#Others              9
#Endorsement         6
```
