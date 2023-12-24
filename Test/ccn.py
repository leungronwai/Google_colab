import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve



# Importing the dataset
dataset = pd.read_csv('creditcard.csv')
dataset.head()
dataset.shape
dataset.info()
dataset.describe()
dataset.isnull().sum()
dataset.Class.value_counts()
dataset.Class.value_counts(normalize=True)
dataset.groupby('Class').mean()
dataset.corr()
dataset.corr()['Class'].sort_values()
dataset.corr()['Class'].sort_values(ascending=False)
dataset.corr()['Class'].sort_values(ascending=False).plot(kind='bar')
plt.show()
dataset.hist(figsize=(20,20))
plt.show()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X.shape
y.shape

