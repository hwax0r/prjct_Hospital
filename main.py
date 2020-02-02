import os
import time


def cls():
    if os.name.lower() == 'windows':
        clear = lambda: os.system('cls')
        return clear()
    else: 
        clear = lambda: os.system('clear')
        return clear()

    
def signin_register_screen():
    cls()
    print('Hi, pjct_Hospital employees')
    print('you have to 1:login or 2:register')
    while True:
        choose = input('1 or 2: ')
        if choose == '1':
            cls()
            return signin()
        elif choose == '2':
            cls()
            return register()
        else:
            print('Error')
            print('there are no such option')
            time.sleep(4)
            cls()
            return signin_register_screen

    
def signin():
    fin = open('employees/accounts.txt','rt')
    print('This is SignIn screen \n')
    login = input('login: ')
    passwd = input('password: ')
    string = login + ' '+ passwd
    while True:
        line = fin.readline()
        if string == line:
            cls()
            return first_scene 
        elif line == '' or ' ':
            cls()
            print('Error')
            print('There are no such login or password or even account')
            print('Please contact your system administrator')
            time.sleep(10)
            cls()
            return signin_register_screen()


def register():
    cls()
    fout = open('employees/accounts.txt','a')
    print('This is Register screen \n')
    login = input('login: ')
    passwd = input('password: ')
    if find_employee_account(login, passwd):
        cls()
        print('Error')
        #print('This account already exists')
        print('Please change your login and password')
        time.sleep(2)
        cls()
        print('Do you want to \n')
        print('1:move back to login/register screen \n')
        print('or \n')
        print('2:register one more time? \n')
        while True:
            user_input = input('1 or 2: ')
            if user_input == '1':
                return signin_register_screen()
            elif user_input == '2':
                return register()
            else:
                print('Error')
                print('There are no such option')
                time.sleep(1)
    else:
        fout.write(login + ' ' + passwd + '\n')

def find_employee_account(login, passwd):
    fin = open('employees/accounts.txt','rt')
    string = login + ' ' + passwd
    while True:
        line = fin.readline()
        if string == line:
            return True
        else:
            return False



register()

    
    