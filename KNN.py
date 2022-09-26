import csv
import numpy
import operator
import matplotlib.pyplot as plt
def normlize(list_n,num,train):
    minElement = numpy.amin(list_n)
    maxElement=numpy.amax(list_n)
    for i in range(1,len(train)):
        train[i][num]=(train[i][num]-minElement)/(maxElement-minElement)
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
    return t,f_9,f_10,f_11,f_12
def predict(list_d,test,train,z):
    f = open("KNN.txt", "a")
    k=1
    s0="test,train num:"+str(z)+" k="+str(k)+"\n"
    f.write(s0)
    print("test,train num:",z)
    l=[]
    while k<51:
        e=0
        print("k=",k)
        for t in range(0,len(test)-1):
            s4="test("+str(t+1)+"):"+str(test[t+1])+"\n"
            f.write(s4)
            d={}
            d['H']=0
            d['M']=0
            d['L']=0
            for a in range(0,k):
                x,y=list_d[t][a]
                s=str(a+1)+".index:"+str(x)+" ->distance:"+str(y)+" label->"+train[x][16]+"\n"
                f.write(s)
                if train[x][16]=='H':
                   d['H']+=1
                elif train[x][16]=='M':
                    d['M']+=1
                elif train[x][16]=='L':
                    d['L']+=1
            Keymax = max(d, key=d.get)
            s2=str(d)+" predicted:"+Keymax+" Actual:"+test[t+1][16]+"\n"
            f.write(s2)
            if Keymax!=test[t+1][16]:
                e+=1
        Error=e/(len(test)-1)
        s3="num of error:"+str(e)+" percent:"+str(Error)+"\n"
        print("num of error:",e," percent:",Error)
        y=[k,e]
        l.append(y)
        f.write(s3)
        if k ==1: k+=4
        else:k+=5
    return l
def distance(test,train):
    list_d=[]
    d_d={}
    for i in range(1,len(test)):
        for j in range(1,len(train)):
            d_sum=0
            for k in range(0,16):
                d=0
                if k==9 or k==10 or k==10 or k==11:
                    if test[i][k]>=train[j][k]:
                        d=test[i][k]-train[j][k]
                    else:
                        d=train[j][k]-test[i][k]
                else:
                    if test[i][k]==train[j][k]:
                        d= 0
                    else:
                        d= 1
                d_sum+=d
            d_d[j]=d_sum
        sorted_d={}
        sorted_d = sorted(d_d.items(), key=operator.itemgetter(1))
        list_d.append(sorted_d)
    return list_d
            
def KNN(count):
    train_p=[]
    s="train"+ str(count)+".csv"
    with open(s) as f:
            reader = csv.reader(f)
            for i in reader:
                train_p.append(i)
    test_p=[]
    train,f_9,f_10,f_11,f_12=listnumfeaturs(train_p)
    normlize(f_9,9,train)
    normlize(f_10,10,train)
    normlize(f_11,11,train)
    normlize(f_12,12,train)
    s2="test"+ str(count)+".csv"
    with open(s2) as f:
            reader = csv.reader(f)
            for i in reader:
                test_p.append(i)
    test,ft_9,ft_10,ft_11,ft_12=listnumfeaturs(test_p)
    normlize(ft_9,9,test)
    normlize(ft_10,10,test)
    normlize(ft_11,11,test)
    normlize(ft_12,12,test)
    list_d=distance(test,train)
    l=[]
    l=predict(list_d,test,train,count)
    print("__________________________________")
    return l
def showplt(list_ke):
    x=[]
    y=[]
    for j in range(0,len(list_ke[0])):
        sum_err=0
        for i in list_ke:
            sum_err+=i[j][1]
            k=i[j][0]
        mean=sum_err/5
        y.append(mean)
        x.append(k)
    plt.plot(x, y, '.-')
    plt.xlabel('K')
    plt.ylabel('Mean of Error')
    print("for k=",1,"mean of error",y[0])
    for i in range(1,len(y)):
        print("for k=",(i)*5,"mean of error",y[i])

f = open("KNN.txt", "w")
f.close()
list_ke=[]
for i in range(0,5):
    l=KNN(i)
    list_ke.append(l)
showplt(list_ke)
       
        
        
        
    


            