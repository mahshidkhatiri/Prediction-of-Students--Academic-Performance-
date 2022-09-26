import csv
import numpy as np
#def std(l,m):
#    x=0.0
#    for i in l:
#        x+=(i-m)**2
#    x=x/(len(l)-1)
#   x=x**(0.5)
#   return x
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
def P(x,count,train):
    count_x=0
    index=[]
    for i in range(1,len(train)):
        if train[i][16]==x:
            count_x+=1
            index.append(i)
    return count_x/(len(train)-1),index

def countnominal(train,list_x):
    d={0:{'M':0,'F':0},
       1:{'KW':0,'lebanon':0,'Egypt':0,'USA':0,'venzuela':0,'Jordan':0,'SaudiArabia':0,'Iran':0,'Tunis':0,'Morocco':0,'Syria':0,'Palestine':0,'Iraq':0,'Lybia':0},
       2:{'KuwaIT':0,'lebanon':0,'Egypt':0,'USA':0,'venzuela':0,'Jordan':0,'SaudiArabia':0,'Iran':0,'Tunis':0,'Morocco':0,'Syria':0,'Palestine':0,'Iraq':0,'Lybia':0},
       3:{'lowerlevel':0,'MiddleSchool':0,'HighSchool':0},
       4:{'G-01':0,'G-02':0,'G-03':0,'G-04':0,'G-05':0,'G-06':0,'G-07':0,'G-08':0,'G-09':0,'G-10':0,'G-11':0,'G-12':0},
       5:{'A':0,'B':0,'C':0},
       6:{'IT':0,'Math':0,'Arabic':0,'Science':0,'English':0,'Quran':0,'Spanish':0,'French':0,'History':0,'Biology':0,'Chemistry':0,'Geology':0},
       7:{'F':0,'S':0},
       8:{'Father':0,'Mum':0},
       13:{'Yes':0,'No':0},
       14:{'Good':0,'Bad':0},
       15:{'Under-7':0,'Above-7':0}}
    for i in d:
        for j in list_x:
            if train[j][i] in d[i]:
                d[i][train[j][i]]+=1
    
    return d
def forbid0probeblity(P):
    for b in [0,1,2]:
        for i in P[b]:
            for j in P[0][i]:
                if P[b][i][j]==0:
                    for f in [0,1,2]:
                        for j in P[0][i]:
                            P[f][i][j]+=1
    return P
def numeric(train,list_x):
    d={9:{'mean':0,'std':0},10:{'mean':0,'std':0},11:{'mean':0,'std':0},12:{'mean':0,'std':0}}
    for i in d:
        x=[]
        for j in list_x:
            x.append(train[j][i])
        d[i]['mean']=np.mean(x)
        d[i]['std']=np.std(x)
    
    return d
def possibility(test,dno,dnu,px):
    p=1
    for i in dno:
        sum_f=0
        count=0
        for j in dno[i]:
            sum_f+=dno[i][j]
            if j==test[i]:
                count=dno[i][j]
        p=p*(count/sum_f)
    z=0
    for i in dnu:
        pi=np.pi #eshtebah dar formoul dashtam
        z=1/((np.power(2*pi, 0.5))*dnu[i]['std'])
        e=np.exp(-1*(np.power((test[i]-dnu[i]['mean']),2))/(2*np.power(dnu[i]['std'],2)))
        p=p*e*z
    f = open("naive_bayes.txt", "a")
    s=str(p)+"\n"
    f.write(s)
    return p
    
def predict(test,PNO_X,PNU_X,P_X):
    f = open("naive_bayes.txt", "a")
    max_p=0
    b=0
    for i in range(0,len(P_X,)):
        x=possibility(test,PNO_X[i],PNU_X[i],P_X[i])
        if x> max_p:
            max_p=x
            b=i
    s="max_p="+str(max_p)+"\n"
    f.write(s)
    return b

def naive_bayes(count):
    ff = open("naive_bayes.txt", "a")
    train_p=[]
    s="train"+ str(count)+".csv"
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
    P_X=[]
    X_index=[]
    PNO_X=[]
    for x in ['H','M','L']:
        x,y=P(x,count,train)
        P_X.append(x)
        X_index.append(y)
    for x in [0,1,2]:
        PNO_X.append(countnominal(train,X_index[x]))
    forbid0probeblity(PNO_X)
    PNU_X=[]
    err=0
    for x in [0,1,2]:
        PNU_X.append(numeric(train,X_index[x]))
    for a in range(1,len(test)):
        predicted_i=predict(test[a],PNO_X,PNU_X,P_X)
        predicted=''
        if predicted_i==0:
            predicted='H'
        elif predicted_i==1:
            predicted= 'M'
        elif predicted_i==2:
            predicted= 'L'
        s='predicted:'+predicted+' actual:'+test[a][16]+"\n"
        ff.write(s)
        
        if predicted!=test[a][16]:
            err+=1
    s2='_____________________________'+"\n"
    ff.write(s2)           
    return err,len(test)
f = open("naive_bayes.txt", "w")
f.close()
mean=0
for i in range(0,5):  
    e,tl=naive_bayes(i)
    print("Error in test", i,'=',e)
    mean+=e
meane=mean/5
pe=meane/(tl-1)
print("count of error:",meane,"error posibility:",pe)