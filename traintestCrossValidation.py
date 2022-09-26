import csv
def Append_index_in_list(list_c,lable,train):
    for i in range(1,len(train)):
        if train[i][16]==lable:
            list_c.append(i)
def separate_test_train(a,b,c,train_p):
    ta=len(a)/5
    tb=len(b)/5
    tc=len(c)/5
    start_a=0
    start_b=0
    start_c=0
    for j in range(0,5):
        test=[]
        train=[]
        train.append(train_p[0])
        test.append(train_p[0])
        lasta=start_a+ta
        lastb=start_b+tb
        lastc=start_c+tc
        if start_a==int(start_a):
            ia=start_a
        else:
            ia=int(start_a)+1

        for i in range(ia,int(lasta)):
            test.append(train_p[a[i]])
        for i in range(0,len(a)):
            if i<start_a or i>= int(lasta):
                train.append(train_p[a[i]])
        if start_b==int(start_b):
            ib=start_b
        else:
            ib=int(start_b)+1
        for i in range(ib,int(lastb)):
            test.append(train_p[b[i]])
        for i in range(0,len(b)):
            if i<start_b or i>= int(lastb):
                train.append(train_p[b[i]])
        if start_c==int(start_c):
            ic=start_c
        else:
            ic=int(start_c)+1
        for i in range(ic,int(lastc)):
            test.append(train_p[c[i]])
        for i in range(0,len(c)):
            if i<start_c or i>= int(lastc):
                train.append(train_p[c[i]])
        start_a=start_a+ta
        start_b=start_b+tb
        start_c=start_c+tc
        s="train"+ str(j)+".csv"
        s1="test"+ str(j)+".csv"
        with open(s, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in train:
                writer.writerow(i)
        with open(s1, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in test:
                writer.writerow(i)
        
        
def make_train_test(file):
    train=[]
    with open(file) as f:
        reader = csv.reader(f)
        for i in reader:
            train.append(i)
    f = open("v.txt", "w")
    f.close()
    list_class_L=[]
    list_class_M=[]
    list_class_H=[]
    Append_index_in_list(list_class_L,"L",train)
    Append_index_in_list(list_class_M,"M",train)
    Append_index_in_list(list_class_H,"H",train)
    separate_test_train(list_class_L,list_class_H,list_class_M,train)
    f.close()
    
list= make_train_test('Students Academic Performance Dataset.csv')