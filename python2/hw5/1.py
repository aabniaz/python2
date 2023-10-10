import re
import json

def save_to_txt(db):
    with open('user_db.txt', 'w') as file:
        json.dump(db, file)

def load_from_txt():
    try:
        with open('user_db.txt', 'r') as file:
            db = json.load(file)
    except FileNotFoundError:
        db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}
    return db

def show_db(db):
    print(db)

def change_name(db, old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')
    
    db[new_name] = db.pop(old_name)
    save_to_txt(db)

def add_user(db, name, password):
    while name in db.keys():
        name = input('Please choose another name: ')

    if check_password(password):
        db[name] = password
        save_to_txt(db)
        print(f'User {name} added successfully.')

def check_password(password):
    count = 0

    while count != 2:
        if len(password) >= 6 and \
                re.search(r'[A-Z]', password) and \
                re.search(r'[a-z]', password) and \
                re.search(r'[@#$%^&]', password) and \
                re.search(r'\d', password):
            count += 1
        else:
            password = input('Enter another password: ')

    return True

def change_password(db, name, old_password):
    if name in db:
        while old_password != db[name]:
            old_password = input('Wrong password! Try again: ')

        new_password = input('Enter the new password: ')
        if check_password(new_password):
            db[name] = new_password
            save_to_txt(db)
            print(f'Password for user {name} changed successfully.')
    else:
        print(f'User {name} does not exist in the database.')

print("Welcome to the user's database!")

while True:
    action = input("What would you like to do? show db/add User/change Name/change Password/exit: ")

    if action == 'show db':
        db = load_from_txt()  
        show_db(db)
    elif action == 'add User':
        name = input('Enter name: ')
        password = input('Enter password: ')
        add_user(db, name, password)
        show_db(db)
    elif action == 'change Name':
        old_name = input('Enter the old name: ')
        new_name = input('Enter the new name: ')
        password = input('Enter the password: ')
        change_name(db, old_name, new_name, password)
        show_db(db)
    elif action == 'change Password':
        name = input('Enter the name: ')
        old_password = input('Enter the old password: ')
        change_password(db, name, old_password)
        show_db(db)
    elif action == 'exit':
        break
    else:
        print('Invalid action. Please choose a valid action.')

print('Goodbye!')
