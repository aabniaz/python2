import tkinter as tk
from tkinter import Label, messagebox
import re
import json

# Function to load the database from the 'user_db.txt' file
def load_from_txt():
    try:
        with open('user_db.txt', 'r') as file:
            db = json.load(file)
    except FileNotFoundError:
        db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}
    return db

# Function to save the database to the 'user_db.txt' file
def save_to_txt(db):
    with open('user_db.txt', 'w') as file:
        json.dump(db, file)

# Function to check if password meets criteria
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

# Function to add a user
def add_user(db, name, password):
    while name in db.keys():
        name = input('Please choose another name: ')

    if check_password(password):
        db[name] = password
        save_to_txt(db)
        print(f'User {name} added successfully.')

# Function to change a user's name
def change_name(db, old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')

    db[new_name] = db.pop(old_name)
    save_to_txt(db)

# Function to change a user's password
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

root = tk.Tk()
root.title("User Database")
widget = Label(None, text='"Welcome to the users database!"')
widget.pack()

# Create and place GUI widgets
"""show_db_button = tk.Button(root, text="Show Database", command=show_db_gui)
show_db_button.pack()"""

add_name_label = tk.Label(root, text="New User Name:")
add_name_label.pack()
add_name_entry = tk.Entry(root)
add_name_entry.pack()

add_password_label = tk.Label(root, text="New User Password:")
add_password_label.pack()
add_password_entry = tk.Entry(root)
add_password_entry.pack()

add_user_button = tk.Button(root, text="Add User", command=add_user_gui)
add_user_button.pack()

old_name_label = tk.Label(root, text="Old User Name:")
old_name_label.pack()
old_name_entry = tk.Entry(root)
old_name_entry.pack()

new_name_label = tk.Label(root, text="New User Name:")
new_name_label.pack()
new_name_entry = tk.Entry(root)
new_name_entry.pack()

change_name_password_label = tk.Label(root, text="Password:")
change_name_password_label.pack()
change_name_password_entry = tk.Entry(root)
change_name_password_entry.pack()

change_name_button = tk.Button(root, text="Change Name", command=change_name_gui)
change_name_button.pack()

change_password_name_label = tk.Label(root, text="User Name:")
change_password_name_label.pack()
change_password_name_entry = tk.Entry(root)
change_password_name_entry.pack()

old_password_label = tk.Label(root, text="Old Password:")
old_password_label.pack()
old_password_entry = tk.Entry(root)
old_password_entry.pack()

change_password_button = tk.Button(root, text="Change Password", command=change_password_gui)
change_password_button.pack()

db_display = tk.Text(root, height=10, width=50)
db_display.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
