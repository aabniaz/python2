import re
import json

# Load the existing user data from a file if it exists, or initialize an empty dictionary
try:
    with open('user_db.json', 'r') as file:
        db = json.load(file)
except FileNotFoundError:
    db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}

def save_db():
    with open('user_db.json', 'w') as file:
        json.dump(db, file)

def show_db():
    print(db)

def change_name(old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')

    db[new_name] = db.pop(old_name)
    save_db()

def add_user(name, password):
    while name in db.keys():
        name = input('Please choose another name: ')

    if check_password(password):
        db[name] = password
        save_db()  # Save the updated database after adding a user
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

def change_password(name, old_password):
    if name in db:
        while old_password != db[name]:
            old_password = input('Wrong password! Try again: ')

        new_password = input('Enter the new password: ')
        if check_password(new_password):
            db[name] = new_password
            save_db()  # Save the updated database after changing the password
            print(f'Password for user {name} changed successfully.')
    else:
        print(f'User {name} does not exist in the database.')

print("Welcome to the user's database!")
action = input("What would you like to do? show db/add User/change Name/change Password: ")

if action == 'show db':
    show_db()
elif action == 'add User':
    name = input('Enter name: ')
    password = input('Enter password: ')
    add_user(name, password)
    show_db()  # Show the updated database after adding a user
elif action == 'change Name':
    old_name = input('Enter the old name: ')
    new_name = input('Enter the new name: ')
    password = input('Enter the password: ')
    change_name(old_name, new_name, password)
    show_db()  # Show the updated database after changing a name
elif action == 'change Password':
    name = input('Enter the name: ')
    old_password = input('Enter the old password: ')
    change_password(name, old_password)
    show_db()  # Show the updated database after changing a password
else:
    print('Invalid action. Please choose a valid action.')
