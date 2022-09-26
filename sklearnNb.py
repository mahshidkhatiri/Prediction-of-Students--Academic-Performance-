import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import normalize
from prettytable import PrettyTable 
from sklearn.naive_bayes import GaussianNB
df = pd.read_csv('Students Academic Performance Dataset.csv')
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=True)
nominal=['gender', 'NationalITy', 'PlaceofBirth', 'StageID', 'GradeID',
       'SectionID', 'Topic', 'Semester', 'Relation','ParentAnsweringSurvey', 'ParentschoolSatisfaction',
       'StudentAbsenceDays']
numeric=['raisedhands','VisITedResources', 'AnnouncementsView', 'Discussion']
enc = OneHotEncoder(handle_unknown='ignore')

for i in numeric:
    z=normalize([df[i]])
    df[i]=z[0]
x=df.drop('Class', axis='columns')
column_trans = make_column_transformer((OneHotEncoder(sparse=False),nominal),remainder='passthrough')
x=(column_trans.fit_transform(x))
y=df['Class']
kfold=[]
head =['test','var_smoothing','Error']
mytable1 = PrettyTable(head)
mytable2= PrettyTable(head)
mytable3= PrettyTable(head)
mytable4= PrettyTable(head)
num=1
for train_index, test_index in skf.split(x, y):
    x_train=[]
    y_train=[]
    x_test=[]
    y_test=[]
    for i in train_index.tolist():
        x_train.append(x[i])
        y_train.append(y[i])
    for i in test_index.tolist():
        x_test.append(x[i])
        y_test.append(y[i])
    clf = GaussianNB()
    clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    error=0
    for m in range(0,len(y_test)):
        if y_test[m] != z[m]:
            error+=1
    d=[num,'default',error]
    mytable1.add_row(d)
    clf = GaussianNB(var_smoothing=10)
    clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    error=0
    for m in range(0,len(y_test)):
        if y_test[m] != z[m]:
            error+=1
    d=[num,'10',error]
    mytable2.add_row(d)
    clf = GaussianNB(var_smoothing=3)
    clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    error=0
    for m in range(0,len(y_test)):
        if y_test[m] != z[m]:
            error+=1
    d=[num,'3',error]
    mytable3.add_row(d)
    clf = GaussianNB(var_smoothing=0.02)
    clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    error=0
    for m in range(0,len(y_test)):
        if y_test[m] != z[m]:
            error+=1
    d=[num,'0.02',error]
    mytable4.add_row(d)
    num+=1
print(mytable1,mytable2,mytable3,mytable4)   