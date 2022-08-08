from data_create import get_surname, get_adress

def adress_input():
    
    surname = get_surname()
    if surname: adress = get_adress()
    fam_id = 0
    with open('C:\\Users\\mob19\\OneDrive\\Рабочий стол\\Python_hw8\\Bots\\1.txt', 'r') as families:
        fam_id = [i[0] for i in families if surname in i][0]
    with open('C:\\Users\\mob19\\OneDrive\\Рабочий стол\\Python_hw8\\Bots\\3.txt', 'a', encoding='utf-8') as file:
        file.write(f'{" "};{fam_id};{surname};{adress}\n')

adress_input()

