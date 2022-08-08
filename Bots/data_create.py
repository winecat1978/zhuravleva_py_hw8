def get_surname():
    got_surname = str(input("Please, print your surname: "))
    with open('C:\\Users\\mob19\\OneDrive\\Рабочий стол\\Python_hw8\\Bots\\1.txt', 'r') as parents:      
        for i in parents:
            if got_surname in i:
                print ("Yes, we found you")
                return got_surname
        else:
            print("Sorry, you aren't in our database!")
            pass

def get_adress():
    got_adress = str(input("Please, print your adress: "))
    return got_adress
