import csv

data=[]

with open('juneroute.csv',newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    for row in reader:
        #print(row)
        dataTuple = ()
        for x in row:
            y = list(dataTuple)
            y.append(x)
            dataTuple = tuple(y)
        data.append(dataTuple)
    searchCriteria = input("Enter your search criteria: ")
    for row in data:
        if searchCriteria in row:
            print(row)
        #print(row)
        #print(','.join(row))
    