from pathlib import Path
import time
import os
import getpass
import sys




###############################Initial Variables####################################
#Path for savefile
data_Path = Path.cwd() / Path('data.txt')
#Getting username
username = getpass.getuser()
#Initializing command variable
#test

#Function list
def display():

    os.system('clear')
    #Headers
    top_bottom_border = '*'*50
    print(top_bottom_border)
    print(f"* {'TaskName: ':<20}",end = ' ')
    print(f"{'| Date: ':<8}",end = '')
    print(f"{' '*18}*")
    #FIXME:Print ToDoList here

    print(top_bottom_border)
    print('\n\n')

#FIXME: Add commands
def handleInput(command):
    
    if command == 'help' or command == 'h':
        print('This program can handle a varity of commands')
        print('Type \'(q)uit\' to exit the program')
        print('Type \'(c)lear\ to clear the text and update the table')
        print('Type \'(a)dd\ to schedule a new event')
        print('Type \'(d)one\ to complete and remove a task from the list')
        return
    elif command == 'clear' or command == 'c':
        display()
    elif command == 'add' or command == 'a':
        print('test<5j><5k>')
    elif command == 'quit' or command == 'q':
        sys.exit()


def get_Input():
    user_Input = input('Command: ')
    return user_Input.lower()






def main():
    command = '' 
    if (data_Path.is_file() is not True):
        data_Path.write_text('No data')
        print(f'A new file has been created at: \n{data_Path}\nThis file holds your ToDo List')
        time.sleep(3)

    display()
    #Initial User instructions. I picked this so that new users can get help,
    #but old users won't always see a tutorial
    print(f'Welcome, {username}! Enjoy the program and type "help" if needed')
    
    #Main program loop
    while command != 'quit' or 'q':
        command = get_Input()
        handleInput(command)






if __name__ == '__main__':
    main()

