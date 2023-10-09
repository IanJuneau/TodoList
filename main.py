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
#Initializing ToDoList
ToDoList = []

#Function list
def display():
    os.system('cls' if os.name == 'nt' else 'clear')
    #Useful Variables
    numLength = 3
    dateLength = 8
    taskLength = 20
    totalLength = dateLength+taskLength+numLength + 8
    top_bottom_border = '*'*totalLength


    #Headers
    print(top_bottom_border)
    print(f"* {'Num':<{numLength}}",end = ' |')
    print(f"{'Date: ':<{dateLength}}",end = ' |')
    print(f"{'TaskName: ':<{taskLength}}",end = ' *')
    print('')
    print('*',end = ''); print('-'*(totalLength-2),end = ''); print('*')


    count = 1
    for i in range(0, len(ToDoList), 2):
        print(f"* {str(count):^{numLength}}", end = ' |')
        print(f"{ToDoList[i]:^{dateLength}}", end = ' |')
        print(f"{ToDoList[i+1]:<{taskLength}}", end = ' *')
        print ('')

        count += 1


    print(top_bottom_border)
    print('\n\n')

#FIXME: A command to delete and recreate data.txt if data becomes corrupted
def handleInput(command):
    
    if command == 'help' or command == 'h':
        print('This program can handle a varity of commands')
        print('Type \'(a)dd\ to schedule a new event')
        print('Type \'(c)lear\ to clear the text and update the table')
        print('Type \'(d)one\' to complete a task')
        print('Type \'(q)uit\' to exit the program')
        print('Type \'(s)ave\' to write the ToDoList to "data.txt"')
        return
    elif command == 'clear' or command == 'c':
        display()
    elif command == 'add' or command == 'a':
        temp = input('Please enter the task in the form {mm/dd, Task}')
        
        taskArray = temp.split(',')

        ToDoList.append(taskArray[0].strip())
        ToDoList.append(taskArray[1].strip())


    elif command == 'save' or command == 's':
        save()
    elif command == 'quit' or command == 'q':
        sys.exit()
    elif command == 'done' or command == 'd':
        print('Congratulations on finishing your task! I am very proud of you. What task did you complete?')
        line_number = int(input())
        index2 = line_number*2-2
        index1 = line_number*2-1

        del ToDoList[index1]
        del ToDoList[index2]

def save():
    f = open('data.txt','w')
    f.truncate()

    for i in range(len(ToDoList)):
        f.write(f"{ToDoList[i]}, ")
    
    f.close()

def readData():
    f = open('data.txt')
    temp = f.read()
    
    Data_set = temp.split(',')

    for i in range(len(Data_set)):
        data = Data_set[i].strip()
        if data == '':
            break
        ToDoList.append(data)

def get_Input():
    user_Input = input('Command: ')
    return user_Input.lower()

def main():
    if (data_Path.is_file() is not True):
        data_Path.write_text('12/25, Christmas, ')
    else:
        readData()

    display()
    #Initial User instructions. I picked this so that new users can get help,
    #but old users won't always see a tutorial
    print(f'Welcome, {username}! Enjoy the program and type "(h)elp" if needed')
    
    #Main program loop
    while True:
        command = get_Input()
        handleInput(command)

if __name__ == '__main__':
    main()

