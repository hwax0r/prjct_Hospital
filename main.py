import os
import time
import hashlib


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
    cls()
    print('This is SignIn screen \n')
    login = input('login: ')
    passwd = input('password: ')
    if find_employee_account(login, passwd):
        cls()
        fin.close()
        return create_find_edit_patient_card() 
    else:
        cls()
        print('Error')
        print('There are no such login or password or even account')
        print('Please contact your system administrator')
        time.sleep(10)
        cls()
        fin.close()
        return signin_register_screen()

def register():
    cls()
    fout = open('employees/accounts.txt','w')
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
                fout.close()
                return signin_register_screen()
            elif user_input == '2':
                fout.close()
                return register()
            else:
                print('Error')
                print('There are no such option')
                time.sleep(1)
    else:
        fout.write(login + ' ' + passwd)
        fout.write('\n')
        fout.close()
        return signin_register_screen()

def find_employee_account(login, passwd)-> bool:
    '''this func searches through the file with login&passwords
    for employees and returns True if account exists'''

    fin = open('employees/accounts.txt','rt')
    string = [login, passwd]
    while True:
        line = fin.readline().split()
        if string == line:
            fin.close()
            return True
        elif line == []:
            fin.close()
            return False

def create_find_edit_patient_card():
    print('now you can create or find or edit patient card\n')
    print('Choose option: ')
    print('\t 1: create patient card')
    print('\t 2: find patient card')
    print('\t 3: edit patient card')
    user_input = input('choose 1 or 2 or 3: ')
    if user_input == '1':
        return create_patient_card()
    elif user_input == '2':
        return find_patient_card()
    elif user_input == '3':
        return edit_patien_card()
    else:
        print('\n\n\n\n')
        print('Error')
        print('wrong input')
        time.sleep(5)
        cls()
        return create_find_edit_patient_card()

def create_patient_folder(string: str) -> str:
    string_utf8 = string.encode(encoding='utf-8')
    encoded = hashlib.md5(string_utf8)
    folder_name = encoded.hexdigest()
    current_dir = str(os.getcwd())
    directory_for_cards = current_dir + '/patients/cards/'
    if not os.path.isdir(directory_for_cards):
        os.mkdir(directory_for_cards)
    os.mkdir(directory_for_cards + folder_name)
    return folder_name


def write_patient_into_db(surname: str, name: str, patronymic: str, birth_date: str) -> str:
    patients_database = open('patients/patientsDatesPaths', 'w')
    string = surname + '|' + name + '|' + patronymic + '|' + birth_date
    patient_card_path = create_patient_folder(string)
    patients_database.write(string + '|' + patient_card_path)
    patients_database.close()
    print('patient successfully added to db')


def create_patient_card():
    pass

def find_patient_card():
    pass

def edit_patien_card():
    #This might be really hard to make in-bash or in-cmd text editor
    pass