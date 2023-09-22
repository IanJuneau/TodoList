from pathlib import Path
import time
import os
import getpass





###############################Initial Variables####################################
#Path for savefile
data_Path = Path.cwd() / Path('data.txt')
#Getting username
username = getpass.getuser()
#Initializing command variable


#Function list
def display():
    os.system('clear')
    #Headers
    print(f"{'TaskName: ':<20}",end = ' ')
    print(f"{'| Date: ':<8}")


def handleInput(command):
    print('yeah')

def get_Input():
    user_Input = input()
    return user_Input






def main():
    command = '' 
    if (data_Path.is_file() is not True):
        data_Path.write_text('No data')
        print(f'A new file has been created at: \n{data_Path}\nThis file holds your ToDo List')
        time.sleep(3)

    display()
    #Initial User instructions. I picked this so that new users can get help,
    #but old users won't always see a tutorial
    print('\n\n\n')
    print(f'Welcome, {username}! Enjoy the program and type "help" if needed')
    
    #Main program loop
    while command != 'quit' or 'q':
        command = get_Input()
        handleInput(command)






if __name__ == '__main__':
    main()

