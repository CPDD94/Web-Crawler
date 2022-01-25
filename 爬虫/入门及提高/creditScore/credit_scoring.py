import pandas as pd
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = pd.read_csv('cs-training.csv')
data.rename(columns={'Unnamed: 0':'ID'},inplace=True)
data['MonthlyIncome'].fillna(data['MonthlyIncome'].median(),inplace=True)
data['NumberOfDependents'].fillna(data['NumberOfDependents'].mode()[0],inplace=True)
X = data.drop(columns='SeriousDlqin2yrs')
y = data['SeriousDlqin2yrs']
#print(train_data['SeriousDlqin2yrs'].value_counts())
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=123)
#print(Counter(y_train))  #查看标签分布
#查看去重个数
#print(train_data.duplicated().value_counts())   # False    150000
msno.matrix(data)  #作图查看缺失值分布
#plt.show()
## 可以用随机森林等算法来填充缺失值
#print(train_data.isnull().sum()/len(train_data))  # 查看各字段缺失值占比
# print(train_data['MonthlyIncome'].median())  #中位数填充
# print(train_data['NumberOfDependents'].mode()[0])  #众数填充
#画箱体图，看异常值

# corr = train_data.corr()
# plt.figure(figsize=(20,18))
# sns.heatmap(corr,annot=True)
# plt.show()
smote = SMOTE(random_state=123)
X_smoteTrain,y_smoteTrain = smote.fit_resample(X_train,y_train)
RF = SVC(random_state=123)
#RF.fit(X_train,y_train)    #0.8634855082950674
RF.fit(X_smoteTrain,y_smoteTrain)   #0.8424785838877312
y_preb = RF.predict_proba(X_test)
roc1 = roc_auc_score(y_test,y_preb[:,1])
print(roc1)