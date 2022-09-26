import pandas as pd
from sklearn import tree
from sklearn.model_selection import StratifiedKFold
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import normalize
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
head =['criterion','max_depth','max_features', 'random_state','error']
mytable1 = PrettyTable(head)
mytable2= PrettyTable(head)
mytable3= PrettyTable(head)
mytable4= PrettyTable(head)
mytable5= PrettyTable(head)
mytable6= PrettyTable(head)
mytable7= PrettyTable(head)
mytable8= PrettyTable(head)
mytable9= PrettyTable(head)
mytable10= PrettyTable(head)
for train_index, test_index in skf.split(x, y):
    x_train=[]
    y_train=[]
    x_test=[]
    y_test=[]
    d=[]
    for i in train_index.tolist():
        x_train.append(x[i])
        y_train.append(y[i])
    for i in test_index.tolist():
        x_test.append(x[i])
        y_test.append(y[i])
    error=0
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=3,max_features='log2')
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['gini',3,'log2','none',error]
    mytable1.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,max_features='log2')
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['entropy',3,'log2','none',error]
    mytable2.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=6,max_features='log2')
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['gini',6,'log2','none',error]
    mytable3.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=6,max_features='log2')
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['entropy',6,'log2','none',error]
    mytable4.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=12,max_features='sqrt')
    clf = clf.fit(x_train, y_train) 
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['gini',12,'sqrt','none',error]
    mytable5.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=12,max_features='sqrt')
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['entropy',12,'sqrt','none',error]
    mytable6.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,max_features='log2',random_state=2)
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['entropy',3,'log2','2',error]
    mytable7.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,max_features='log2',random_state=3)
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['entropy',3,'log2','3',error]
    mytable8.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=3,max_features='log2',random_state=2)
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['gini',3,'log2','2',error]
    mytable9.add_row(d)
    error=0
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=3,max_features='log2',random_state=3)
    clf = clf.fit(x_train, y_train)
    z=clf.predict(x_test)
    for m in range(0,len(y_test)):
            if y_test[m] != z[m]:
                error+=1
    d=['gini',3,'log2','3',error]
    mytable10.add_row(d)
    

print(mytable1,mytable2,mytable3,mytable4,mytable5,mytable6,mytable7,mytable8,mytable9,mytable10)    