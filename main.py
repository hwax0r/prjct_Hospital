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
    print('Hi, pjct_Hospital employees')
    print('you have to 1:login or 2:register')
    choose = int(input('1 or 2: '))
    if choose == 1:
        cls()
        return signin()
    elif choose == 2:
        cls()
        return register()
    else:
        print('Error')
        print('there are no such option')
        time.sleep(10)
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
            return first_scene ###############################################################
        if line == '' or ' ':
            print('Error')
            print('There are no such login or password or even account')
            print('Please contact your system administrator')
            time.sleep(10)
            cls()
            return signin_register_screen()


def register():
    fout = open('employees/accounts.txt','wt')
    print('This is Register screen \n')
    login = input('login: ')
    passwd = input('password: ')
    fout.write()

    
    