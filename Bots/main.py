database ={}
db = {'parents':1, 'children':2}
def reading_file_to_dict(number_file):
    with open(f'C:\\Users\\mob19\\OneDrive\\Рабочий стол\\Python_hw8\\Bots\\{number_file}.txt', 'r') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = [] #{} - dict Первый столбец
    #for i in data[0].split(';'):
        for i in data:
            database[number_file].append(tuple(i.split(';')))
        #database[count][i] = 

def print_children(surname):
    id = [i[0] for i in database[db['parents']] if surname in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])
    
#import os, sys     Проверяю директорию и путь файла 
#filename = '2.txt'
#print(os.path.abspath(filename))
#app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
#print(os.path.join(app_dir,filename))

reading_file_to_dict(1)
reading_file_to_dict(2)
print(database)

#Вывести всех детей Иванова
print_children('Ivanov')