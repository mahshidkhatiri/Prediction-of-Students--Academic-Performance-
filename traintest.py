import csv
import random
def maketraintest(file_name,count):
    train=[]
    with open(file_name) as f:
        reader = csv.reader(f)
        for i in reader:
            train.append(i)
    test=[]
    test.append(train[0])
    test_len=int(0.2*(len(train)-1))
    for i in range(0,test_len):
        num = random.randint(1,len(train)-1)
        test.append(train[num])
        del train[num]
    s="train"+ str(count)+".csv"
    s1="test"+ str(count)+".csv"
    with open(s, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in train:
                writer.writerow(i)
    with open(s1, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in test:
                writer.writerow(i)
for i in range(0,5):
    maketraintest('Students Academic Performance Dataset.csv',i)
