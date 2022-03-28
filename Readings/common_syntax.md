# Python Commonly-Used Syntax

# Table of contents
- [Table of contents](#table-of-contents)
- [Python](#python)
  - [List](#list)
- [Pandas](#pandas)
- [Numpy](#numpy)
- [Matplotlib](#matplotlib)
- [Sklearn](#sklearn)
  - [Evaluation Metrics](#evaluation-metrics)
# Python
## List
- `list_a[-100:]` get the last 100 items in the list

[(Back to top)](#table-of-contents)

# Pandas
# Numpy
# Matplotlib
# Sklearn
## Pre-processing
### Label Encoding
- To encode the categorical variables to number
```Python
label_enocoder = sklearn.preprocessing.LabelEncoder()
# Encoding "Target" to number 
y_train = label_enocoder.fit_transform(labeled_train_df['label'].values)

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
