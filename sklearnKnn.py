import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
from prettytable import PrettyTable 
df = pd.read_csv('Students Academic Performance Dataset.csv')
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
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
    z=[[x_train,y_train],[x_test,y_test]]
    kfold.append(z)
head =['k','weights','p','error']
myTable = PrettyTable(head)
k=[1,5,10,15,20,25,30,35,40,45,50]
error_l=[]
for n_neighbors in k:
    error=0
    d=[]
    neigh = KNeighborsClassifier(n_neighbors)
    for j in kfold:
        err=0
        neigh.fit(j[0][0], j[0][1])
        z=neigh.predict(j[1][0])
        for i in range(0,len(j[1][1])):
            if j[1][1][i] != z[i]:
                err+=1
        error+=err
    error=(error/5)/len(j[1][1])      
    error_l.append(error)
    d=[str(n_neighbors),'uniform','2',str(error)]
    myTable.add_row(d)
plt.plot(k, error_l)
error_l=[]
for n_neighbors in k:
    error=0
    neigh = KNeighborsClassifier(n_neighbors,weights='distance')
    for j in kfold:
        err=0
        neigh.fit(j[0][0], j[0][1])
        z=neigh.predict(j[1][0])
        for i in range(0,len(j[1][1])):
            if j[1][1][i] != z[i]:
                err+=1
        error+=err
    error=(error/5)/len(j[1][1])       
    error_l.append(error)
    d=[str(n_neighbors),'distance','2',str(error)]
    myTable.add_row(d)
plt.plot(k, error_l)
error_l=[]
for n_neighbors in k:
    error=0
    neigh = KNeighborsClassifier(n_neighbors,p=3)
    for j in kfold:
        err=0
        neigh.fit(j[0][0], j[0][1])
        z=neigh.predict(j[1][0])
        for i in range(0,len(j[1][1])):
            if j[1][1][i] != z[i]:
                err+=1
        error+=err
    error=(error/5)/len(j[1][1])     
    error_l.append(error)
    d=[str(n_neighbors),'uniform','3',str(error)]
    myTable.add_row(d)
plt.plot(k, error_l)
error_l=[]
for n_neighbors in k:
    error=0
    neigh = KNeighborsClassifier(n_neighbors,weights='distance',p=3)
    for j in kfold:
        err=0
        neigh.fit(j[0][0], j[0][1])
        z=neigh.predict(j[1][0])
        for i in range(0,len(j[1][1])):
            if j[1][1][i] != z[i]:
                err+=1
        error+=err
    error=(error/5)/len(j[1][1])      
    error_l.append(error)
    d=[str(n_neighbors),'distance','3',str(error)]
    myTable.add_row(d)
plt.plot(k, error_l)
print(myTable)
