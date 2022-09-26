from sklearn.cluster import KMeans
from sklearn.model_selection import StratifiedKFold
import pandas as pd
from random import randint
from prettytable import PrettyTable
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import normalize
from sklearn.preprocessing import OneHotEncoder 
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
def K_means(j,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                verbose, random_state, copy_x, n_jobs, algorithm):
    kmeans = KMeans(n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                verbose, random_state, copy_x, n_jobs, algorithm)
    kmeans.fit(j[0][0],j[0][1])
    y_cluster=[]
    err=0
    for i in range(0, n_clusters):
        M,L,H=0,0,0
        for f in range(0,len(j[0][0])):
            if kmeans.labels_[f]==i:
                if j[0][1][f]=="M":
                    M+=1
                elif j[0][1][f]=="H":
                    H+=1
                elif j[0][1][f]=="L":
                    L+=1
        if M>L and M>H:
            y_cluster.append("M")
        elif H>M and H>L:
            y_cluster.append("H")
        elif L>M and L>H:
            y_cluster.append("L")
        elif L>M and L==H:
            c=randint(0, 1)
            if c==0:
                y_cluster.append("L")
            else:
                y_cluster.append("H")
        elif L>H and L==M:
            c=randint(0, 1)
            if c==0:
                y_cluster.append("M")
            else:
                y_cluster.append("L")
        elif M>L and M==H:
            c=randint(0, 1)
            if c==0:
                y_cluster.append("M")
            else:
                y_cluster.append("H")
        else:
            c=randint(0, 2)
            if c==0:
                y_cluster.append("M")
            elif c==1:
                 y_cluster.append("L")
            else:
                y_cluster[i].append("H")
    z=kmeans.predict(j[1][0])
    for k in range(0,len(z)):
        if y_cluster[z[k]]!=j[1][1][k]:
            err+=1
    return(err)
def K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm):
    head =['num_test','n_clusters','init', 'n_init',' max_iter', 'tol', 'precompute_distances',
                'verbose', 'random_state', 'copy_x', 'n_jobs', 'algorithm',"ERROR"]
    myTable = PrettyTable(head)
    for i in range(0,5):
        n_clusters=2
        j=kfold[i]
        err=K_means(j,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm)
        d=[i,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm,err]
        myTable.add_row(d)
    print(myTable)   
    myTable = PrettyTable(head)
    for i in range(0,5):
        n_clusters=5
        j=kfold[i]
        err=K_means(j,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm)
        d=[i,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm,err]
        myTable.add_row(d)
    print(myTable)   
    myTable = PrettyTable(head)
    for i in range(0,5):
        n_clusters=10
        j=kfold[i]
        err=K_means(j,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm)
        d=[i,n_clusters,  init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm,err]
        myTable.add_row(d)
    print(myTable)   
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

init='k-means++'
n_init=10
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='random'
n_init=10
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=20
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=30
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=400
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=500
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=300
tol=0.001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=300
tol=0.00001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=False
n_jobs='deprecated'
algorithm='auto'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='full'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"
init='k-means++'
n_init=10
max_iter=300
tol=0.0001
verbose=0
random_state=None
copy_x=True
n_jobs='deprecated'
algorithm='elkan'
precompute_distances='deprecated'
K_M_Test(kfold,init, n_init, max_iter, tol, precompute_distances,
                    verbose, random_state, copy_x, n_jobs, algorithm) 
"______________________________________________________"