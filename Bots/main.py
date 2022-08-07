
database ={}
count = 0
with open('2.txt','r', encoding='utf-8)') as file_1:
    count+=1
    data = [i.split('\n')[0] for i in file_1.readlines()]
    database[count] = {}
    for i in data[0].split(';'):
        database[count][i] = 0
        print(database)
