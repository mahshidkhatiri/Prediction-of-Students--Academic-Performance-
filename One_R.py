import csv
from random import randint
import operator
import matplotlib.pyplot as plt
def listnumfeaturs(t_p):
    t=[]
    f_9=[]
    f_10=[]
    f_11=[]
    f_12=[]
    t.append(t_p[0])
    for i in range(1,len(t_p)):
        t_e=[]
        t_e.extend(t_p[i][:9])
        t_e.append(int(t_p[i][9]))
        f_9.append(int(t_p[i][9]))
        t_e.append(int(t_p[i][10]))
        f_10.append(int(t_p[i][10]))
        t_e.append(int(t_p[i][11]))
        f_11.append(int(t_p[i][11]))
        t_e.append(int(t_p[i][12]))
        f_12.append(int(t_p[i][12]))
        t_e.extend(t_p[i][13:])
        t.append(t_e)
    return t
class tree:
    def __init__(self,feature,j):     
        self.root = feature
        self.col=j
        self.leaves=[]
    def addleaf(self,node):
        self.leaves.append(node)
class node:
    def __init__(self,state,lable):
        self.state=state
        self.lable=lable
    

def inttolable(x):
    if x==0: 
        return 'L'
    elif x==1:
        return 'M'
    else:
        return 'H'

d={0:{'M','F'},
       1:{'KW','lebanon','Egypt','USA','venzuela','Jordan','SaudiArabia','Iran','Tunis','Morocco','Syria','Palestine','Iraq','Lybia'},
       2:{'KuwaIT','lebanon','Egypt','USA','venzuela','Jordan','SaudiArabia','Iran','Tunis','Morocco','Syria','Palestine','Iraq','Lybia'},
       3:{'lowerlevel','MiddleSchool','HighSchool'},
       4:{'G-01','G-02','G-03','G-04','G-05','G-06','G-07','G-08','G-09','G-10','G-11','G-12'},
       5:{'A','B','C'},
       6:{'IT','Math','Arabic','Science','English','Quran','Spanish','French','History','Biology','Chemistry','Geology'},
       7:{'F','S'},
       8:{'Father','Mum'},
       13:{'Yes','No'},
       14:{'Good','Bad'},
       15:{'Under-7','Above-7'}}
def OR(count,astane_p):
    s="train"+ str(count)+".csv"
    train_p=[]
    with open(s) as f:
            reader = csv.reader(f)
            for i in reader:
                train_p.append(i)
    test_p=[]
    s2="test"+ str(count)+".csv"
    with open(s2) as f:
            reader = csv.reader(f)
            for i in reader:
                test_p.append(i)
    train=listnumfeaturs(train_p)
    test=listnumfeaturs(test_p)
    min_error=len(train)
    minf=[]
    t=''
    l_t=[]
    j_t=0
    states=[]
    astane=int(astane_p*(len(train)-1))
    for j in range(0,16):
        error=0
        lable=[]
        if j in[0,1,2,3,4,5,6,7,8,13,14,15]:
            for m in d[j]:
                er=0
                c=0
                class_l=[0,0,0] #L,M,H
                for l in range(1,len(train)):
                    if train[l][j]==m:
                        if train[l][16]=='L':
                            class_l[0]+=1
                        elif train[l][16]=='M':
                            class_l[1]+=1
                        elif train[l][16]=='H':
                            class_l[2]+=1
                if class_l[0]>class_l[1] and class_l[0]>class_l[2]:
                    c=0
                elif class_l[1]>class_l[0] and class_l[1]>class_l[2]:
                    c=1
                elif class_l[2]>class_l[1] and class_l[2]>class_l[0]:
                    c=2
                elif class_l[0]==class_l[1] and class_l[0]>class_l[2]:
                    c=randint(0, 1)
                elif class_l[0]==class_l[2] and class_l[2]>class_l[1]:
                    c=randint(0, 1)
                    if c==1:
                        c=2
                elif class_l[2]==class_l[1] and class_l[1]>class_l[0]:
                    c=randint(1, 2)
                elif class_l[2]==class_l[1] and class_l[1]==class_l[0]:
                    c=randint(0, 2)
                for k in range(0,3):
                    if k!=c:
                        er+=class_l[k]
                lable.append(inttolable(c))
                error+=er
                s_j=d[j]
            
        else:
            list_numeric=[]
            for l in range(1,len(train)):
                list_numeric.append((train[l][j],train[l][16]))
            list_numeric.sort(key = operator.itemgetter(0))
            list_numeric_copy=list_numeric.copy()
            d_1={}
            for v in range(0,len(list_numeric_copy)):
                x,y=list_numeric_copy[v]
                if x in d_1:
                    d_1[x].append(y)
                else:
                    d_1[x]=[y]        
            for l in d_1:
                class_l=[0,0,0] #L,M,H
                for z in d_1[l]:
                    if z=='L':
                        class_l[0]+=1
                    elif z=='M':
                        class_l[1]+=1
                    elif z=='H':
                        class_l[2]+=1
                if class_l[0]>class_l[1] and class_l[0]>class_l[2]:
                    c=0
                elif class_l[1]>class_l[0] and class_l[1]>class_l[2]:
                    c=1
                elif class_l[2]>class_l[1] and class_l[2]>class_l[0]:
                    c=2
                elif class_l[0]==class_l[1] and class_l[0]>class_l[2]:
                    c=randint(0, 1)
                elif class_l[0]==class_l[2] and class_l[2]>class_l[1]:
                    c=randint(0, 1)
                    if c==1:
                        c=2
                elif class_l[2]==class_l[1] and class_l[1]>class_l[0]:
                    c=randint(1, 2)
                elif class_l[2]==class_l[1] and class_l[1]==class_l[0]:
                    c=randint(0, 2)
                d_1[l]=c
            for v in range(0,len(list_numeric_copy)):
                x,y=list_numeric_copy[v]
                list_numeric_copy[v]=(x,inttolable(d_1[x]))
            line=[]
            line_p=[]
            for v in range(0,len(list_numeric_copy)):
                if v!=len(list_numeric_copy)-1:
                    x0,y0=list_numeric_copy[v]
                    x1,y1=list_numeric_copy[v+1]
                    if y0!=y1:
                        line_p.append(list_numeric_copy[v])
                        line.append(line_p)
                        line_p=[]
                    else:
                        line_p.append(list_numeric_copy[v])
                else:
                    line_p.append(list_numeric_copy[v])
                    line.append(line_p)
    
            v=0
            while v<len(line):
                class_l=[0,0,0] #L,M,H
                for i in line[v]:
                    x,y=i
                    if y=='L':
                        class_l[0]+=1
                    elif y=='M':
                        class_l[1]+=1
                    elif y=='H':
                        class_l[2]+=1
                if class_l[0]>=astane or class_l[1]>=astane or class_l[1]>=astane  :
                    if class_l[0]>class_l[1] and class_l[0]>class_l[2]:
                        c=0
                    elif class_l[1]>class_l[0] and class_l[1]>class_l[2]:
                        c=1
                    elif class_l[2]>class_l[1] and class_l[2]>class_l[0]:
                        c=2
                    elif class_l[0]==class_l[1] and class_l[0]>class_l[2]:
                        c=randint(0, 1)
                    elif class_l[0]==class_l[2] and class_l[2]>class_l[1]:
                        c=randint(0, 1)
                        if c==1:
                            c=2
                    elif class_l[2]==class_l[1] and class_l[1]>class_l[0]:
                        c=randint(1, 2)
                    elif class_l[2]==class_l[1] and class_l[1]==class_l[0]:
                        c=randint(0, 2)
                    for z in range(0,len(line[v])):
                        x,y=line[v][z]
                        line[v][z]=(x,inttolable(c))
                    if v>0 :
                        x,y=line[v-1][0]
                        if y==inttolable(c):
                            line[v-1]=line[v-1]+line[v]
                            line.pop(v)
                        else:
                            v=v+1
                    else:
                        v=v+1
                elif v+1!=len(line):
                    line[v+1]=line[v]+line[v+1]
                    line.pop(v)
                else:
                    if class_l[0]>class_l[1] and class_l[0]>class_l[2]:
                        c=0
                    elif class_l[1]>class_l[0] and class_l[1]>class_l[2]:
                        c=1
                    elif class_l[2]>class_l[1] and class_l[2]>class_l[0]:
                        c=2
                    elif class_l[0]==class_l[1] and class_l[0]>class_l[2]:
                        c=randint(0, 1)
                    elif class_l[0]==class_l[2] and class_l[2]>class_l[1]:
                        c=randint(0, 1)
                        if c==1:
                            c=2
                    elif class_l[2]==class_l[1] and class_l[1]>class_l[0]:
                        c=randint(1, 2)
                    elif class_l[2]==class_l[1] and class_l[1]==class_l[0]:
                        c=randint(0, 2)
                    for z in range(0,len(line[v])):
                        x,y=line[v][z]
                        line[v][z]=(x,inttolable(c))
                    
                    x,y=line[v-1][0]
                    if y==inttolable(c):
                        line[v-1]=line[v-1]+line[v]
                        line.pop(v)
                    else:
                        v=v+1
            list_numeric_copy=[]
            for i in line:
                for v in i:
                    list_numeric_copy.append(v)
            for i in range(0,len(list_numeric)):
                if list_numeric_copy[i]!=list_numeric[i]:
                    error=error+1
            lable=[]
            s_j=[]
            z=''
            for i in range(0,len(line)):
                x,y=line[i][0]
                lable.append(y)
            for i in range(0,len(line)):
                if i!=len(line)-1:
                    x0,y0=line[i][-1]
                    x1,y1=line[i+1][0]
                    o=(x1+x0)/2
                    s=[z,o]
                    s_j.append(s)
                    z=o
                else:
                    s=[z,'']
                    s_j.append(s)
        if error<min_error:
            min_error=error
            j_t=j
            states=list(s_j)
            l_t=lable
            minf=[]
        elif min_error==error:
            minf.append(i)
          
    t=tree(train[0][j_t],j_t)
    for i in range(0,len(states)):
        n=node(states[i],l_t[i])
        t.addleaf(n)
    print('astane:',astane_p," test num:",count,' feature:',t.root)
    for i in t.leaves:
        print(i.state,'-class->',i.lable)
    error_t=0
    for i in range(1,len(test)):
        if t.col in [0,1,2,3,4,5,6,7,8,13,14,15]:
            for j in t.leaves:
                if test[i][t.col]==j.state:
                    p_l=j.lable
                    a_l=test[i][16]
                    if p_l!= a_l:
                        error_t+=1
        else:
            for j in t.leaves:
                if j.state[0]=='':
                    if test[i][t.col]<j.state[1]:
                        p_l=j.lable
                        a_l=test[i][16]
                        if p_l!= a_l:
                            error_t+=1
                elif j.state[1]=='':
                    if test[i][t.col]>j.state[0]:
                        p_l=j.lable
                        a_l=test[i][16]
                        if p_l!= a_l:
                            error_t+=1
                else:
                    if test[i][t.col]>j.state[0] and test[i][t.col]<j.state[1]:
                        p_l=j.lable
                        a_l=test[i][16]
                        if p_l!= a_l:
                            error_t+=1
    print( error_t/len(test))           
    return error_t/len(test)

astane=[0.2,0.1,0.05]
er=[]
for i in astane:
    e=0
    for j in range(0,5):
        e+=OR(j,i)
    e=e/5
    er.append(e)
print(er)
plt.plot(astane, er)
