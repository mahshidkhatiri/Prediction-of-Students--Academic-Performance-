from sklearn.linear_model import LogisticRegression
import pandas as pd
from prettytable import PrettyTable
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.compose import make_column_transformer
from sklearn.metrics import classification_report
from sklearn.preprocessing import normalize
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import multilabel_confusion_matrix
df = pd.read_csv('Students Academic Performance Dataset.csv')
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
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
for train_index, test_index in skf.split(x, y):
    x_train=[]
    y_train=[]
    x_test=[]
    y_test=[]
    for i in train_index.tolist():
        list1 = x[i].tolist()
        x_train.append(list1)
        y_train.append(y[i])
    for i in test_index.tolist():
        list1 = x[i].tolist()
        x_test.append(list1)
        y_test.append(y[i])
    z=[[x_train,y_train],[x_test,y_test]]
    kfold.append(z)
head =["test_num",'penalty', 'dual', 'tol','C',"accuracy"]
myTable = PrettyTable(head)
for i in range(0,5):
    print("test num =",i+1)
    j=kfold[i]
    clf =LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None).fit(j[0][0], j[0][1])
    z=clf.predict(j[1][0])
    print(clf.coef_)
    df = { 'H': [1,0,0], 
                  'M': [0,1,0], 
                  'L': [0,0,1]}
    y_p=[]
    for l in z:
        y_p.append(df[l])
    y_t=[]
    for l in j[1][1]:
        y_t.append(df[l])
    cm = multilabel_confusion_matrix(y_t,y_p)
    print("confusion_matrix:\n",cm)
    tn = cm[:, 0, 0]
    tp = cm[:, 1, 1]
    fn = cm[:, 1, 0]
    fp = cm[:, 0, 1]
    print(" tp:",tp,"\n tn:",tn,"\n fn:",fn,"\n fp:",fp)
    print(classification_report(j[1][1],z))
    print("___________________________________________________________")
    acc=accuracy_score(j[1][1],z)
    d=[str(i),'l2','False','0.0001','1.0',str(acc)]
    myTable.add_row(d)
for i in range(0,5):
    print("test num =",i+1)
    j=kfold[i]
    clf =LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.5, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None).fit(j[0][0], j[0][1])
    z=clf.predict(j[1][0])
    print(clf.coef_)
    df = { 'H': [1,0,0], 
                  'M': [0,1,0], 
                  'L': [0,0,1]}
    y_p=[]
    for l in z:
        y_p.append(df[l])
    y_t=[]
    for l in j[1][1]:
        y_t.append(df[l])
    cm = multilabel_confusion_matrix(y_t,y_p)
    print("confusion_matrix:\n",cm)
    tn = cm[:, 0, 0]
    tp = cm[:, 1, 1]
    fn = cm[:, 1, 0]
    fp = cm[:, 0, 1]
    print(" tp:",tp,"\n tn:",tn,"\n fn:",fn,"\n fp:",fp)
    print(classification_report(j[1][1],z))
    print("___________________________________________________________")
    acc=accuracy_score(j[1][1],z)
    d=[str(i),'l2','False','0.0001','1.5',str(acc)]
    myTable.add_row(d)
for i in range(0,5):
    print("test num =",i+1)
    j=kfold[i]
    clf =LogisticRegression(penalty='none', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None).fit(j[0][0], j[0][1])
    z=clf.predict(j[1][0])
    print(clf.coef_)
    df = { 'H': [1,0,0], 
                  'M': [0,1,0], 
                  'L': [0,0,1]}
    y_p=[]
    for l in z:
        y_p.append(df[l])
    y_t=[]
    for l in j[1][1]:
        y_t.append(df[l])
    cm = multilabel_confusion_matrix(y_t,y_p)
    print("confusion_matrix:\n",cm)
    tn = cm[:, 0, 0]
    tp = cm[:, 1, 1]
    fn = cm[:, 1, 0]
    fp = cm[:, 0, 1]
    print(" tp:",tp,"\n tn:",tn,"\n fn:",fn,"\n fp:",fp)
    print(classification_report(j[1][1],z))
    print("___________________________________________________________")
    acc=accuracy_score(j[1][1],z)
    d=[str(i),'none','False','0.0001','1.0',str(acc)]
    myTable.add_row(d)
    

for i in range(0,5):
    print("test num =",i+1)
    j=kfold[i]
    clf =LogisticRegression(penalty='l2', dual=False, tol=0.001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='lbfgs', max_iter=100, multi_class='auto', verbose=0, warm_start=False, n_jobs=None, l1_ratio=None).fit(j[0][0], j[0][1])
    z=clf.predict(j[1][0])
    print(clf.coef_)
    df = { 'H': [1,0,0], 
                  'M': [0,1,0], 
                  'L': [0,0,1]}
    y_p=[]
    for l in z:
        y_p.append(df[l])
    y_t=[]
    for l in j[1][1]:
        y_t.append(df[l])
    cm = multilabel_confusion_matrix(y_t,y_p)
    print("confusion_matrix:\n",cm)
    tn = cm[:, 0, 0]
    tp = cm[:, 1, 1]
    fn = cm[:, 1, 0]
    fp = cm[:, 0, 1]
    print(" tp:",tp,"\n tn:",tn,"\n fn:",fn,"\n fp:",fp)
    print(classification_report(j[1][1],z))
    print("___________________________________________________________")
    acc=accuracy_score(j[1][1],z)
    d=[str(i),'l2','False','0.001','1.0',str(acc)]
    myTable.add_row(d)
print(myTable)
    
    
    
    
    
    
    
    
    
    