import pandas as pd
from apyori import apriori
from prettytable import PrettyTable 
store_data = pd.read_csv('store_data.csv', header=None)
records = []
for i in range(0, 7501):
    list_a=[]
    for j in range(0, 20):
        if str(store_data.values[i,j])!="nan":
            list_a.append(store_data.values[i,j])
    records.append(list_a)
head =['min_support', 'min_confidence', 'min_lift', 'min_length','rule num']
myTable = PrettyTable(head)
association_rules = apriori(records, min_support=0.01, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
d=['0.01','0.2','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
list_as=[]
for item in association_results:
    pair = item[0] 
    items = [x for x in pair]
    list_r=[item[1],item[2][0][2],items[0] ,items[1],item[2][0][2]]
    list_as.append(list_r)
d=['0.0045','0.2','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0009, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
d=['0.0009','0.2','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0009, min_confidence=0.01, min_lift=3, min_length=2)
association_results = list(association_rules)
d=['0.0009','0.01','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.1, min_lift=3, min_length=2)
association_results = list(association_rules)
d=['0.0045','0.1','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.4, min_lift=3, min_length=2)
association_results = list(association_rules)
d=['0.0045','0.3','3','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=4, min_length=2)
association_results = list(association_rules)
d=['0.0045','0.2','4','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=2, min_length=2)
association_results = list(association_rules)
d=['0.0045','0.2','2','2',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=3)
association_results = list(association_rules)
d=['0.0045','0.2','3','3',str(len(association_results))]
myTable.add_row(d)
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=1)
association_results = list(association_rules)
d=['0.0045','0.2','3','1',str(len(association_results))]
myTable.add_row(d)
print(myTable)
sorted_list_sup = sorted(list_as, key=lambda x:x[0], reverse=True)
print("____________________________Support_______________________________")
if len(sorted_list_sup)>9:
    for j in range(0,10):
        i=sorted_list_sup[j]
        print(str(j+1)+" Rule: " + i[2] + " -> " + i[3])
        print("Support: " + str(i[0]))
        print("Confidence: " + str(i[1]))
        print("lift: " + str(i[4]))
        print("=====================================")
else:
    for j in range(0,len(sorted_list_sup)):
        i=sorted_list_sup[j]
        print(str(j+1)+" Rule: " + i[2] + " -> " + i[3])
        print("Support: " + str(i[0]))
        print("Confidence: " + str(i[1]))
        print("lift: " + str(i[4]))
        print("=====================================")
print("____________________________Confidence______________________________")
sorted_list_conf = sorted(list_as, key=lambda x:x[1], reverse=True)
if len(sorted_list_conf)>9:
    for j in range(0,10):
        i=sorted_list_conf[j]
        print(str(j+1)+" Rule: " + i[2] + " -> " + i[3])
        print("Support: " + str(i[0]))
        print("Confidence: " + str(i[1]))
        print("lift: " + str(i[4]))
        print("=====================================")
else:
    for j in range(0,len(sorted_list_conf)):
        i=sorted_list_conf[j]
        print(str(j+1)+" Rule: " + i[2] + " -> " + i[3])
        print("Support: " + str(i[0]))
        print("Confidence: " + str(i[1]))
        print("lift: " + str(i[4]))
        print("=====================================")