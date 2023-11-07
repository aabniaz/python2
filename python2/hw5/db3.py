import tkinter as tk
import re
import json

def load_from_txt():
    try:
        with open('user_db.txt', 'r') as file:
            db = json.load(file)
    except FileNotFoundError:
        db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}
    return db

def save_to_txt(db):
    with open('user_db.txt', 'w') as file:
        json.dump(db, file)

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

def add_user(db, name, password):
    while name in db.keys():
        name = input('Please choose another name: ')
    if check_password(password):
        db[name] = password
        save_to_txt(db)
        print(f'User {name} added successfully.')

def change_name(db, old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')

    db[new_name] = db.pop(old_name)
    save_to_txt(db)

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

def show_db_window():
    show_db = tk.Toplevel(root)
    show_db.title("Show Database")

    db = load_from_txt()
    db_display = tk.Text(show_db, height=10, width=50)
    db_display.pack()

    for name, password in db.items():
        db_display.insert(tk.END, f'{name}: {password}\n')

    exit_button = tk.Button(show_db, text="Exit", command=show_db.destroy)
    exit_button.pack()

def add_user_window():
    add_user = tk.Toplevel(root)
    add_user.title("Add User")

    add_name_label = tk.Label(add_user, text="New User Name:")
    add_name_label.pack()
    add_name_entry = tk.Entry(add_user)
    add_name_entry.pack()

    add_password_label = tk.Label(add_user, text="New User Password:")
    add_password_label.pack()
    add_password_entry = tk.Entry(add_user)
    add_password_entry.pack()

    add_user_button = tk.Button(add_user, text="Add User", command=lambda: add_user_gui(add_name_entry.get(), add_password_entry.get()))
    add_user_button.pack()

    exit_button = tk.Button(add_user, text="Exit", command=add_user.destroy)
    exit_button.pack()

def add_user_gui(name, password):
    db = load_from_txt()
    add_user(db, name, password)
    save_to_txt(db)

def change_name_window():
    change_name = tk.Toplevel(root)
    change_name.title("Change Name")

    old_name_label = tk.Label(change_name, text="Old User Name:")
    old_name_label.pack()
    old_name_entry = tk.Entry(change_name)
    old_name_entry.pack()

    new_name_label = tk.Label(change_name, text="New User Name:")
    new_name_label.pack()
    new_name_entry = tk.Entry(change_name)
    new_name_entry.pack()

    change_name_password_label = tk.Label(change_name, text="Password:")
    change_name_password_label.pack()
    change_name_password_entry = tk.Entry(change_name)
    change_name_password_entry.pack()

    change_name_button = tk.Button(change_name, text="Change Name", command=lambda: change_name_gui(old_name_entry.get(), new_name_entry.get(), change_name_password_entry.get()))
    change_name_button.pack()

    exit_button = tk.Button(change_name, text="Exit", command=change_name.destroy)
    exit_button.pack()

def change_name_gui(old_name, new_name, password):
    db = load_from_txt()
    change_name(db, old_name, new_name, password)
    save_to_txt(db)

def change_password_window():
    change_password = tk.Toplevel(root)
    change_password.title("Change Password")

    change_password_name_label = tk.Label(change_password, text="User Name:")
    change_password_name_label.pack()
    change_password_name_entry = tk.Entry(change_password)
    change_password_name_entry.pack()

    old_password_label = tk.Label(change_password, text="Old Password:")
    old_password_label.pack()
    old_password_entry = tk.Entry(change_password)
    old_password_entry.pack()

    change_password_button = tk.Button(change_password, text="Change Password", command=lambda: change_password_gui(change_password_name_entry.get(), old_password_entry.get()))
    change_password_button.pack()

    exit_button = tk.Button(change_password, text="Exit", command=change_password.destroy)
    exit_button.pack()

def change_password_gui(name, old_password):
    db = load_from_txt()
    change_password(db, name, old_password)
    save_to_txt(db)

root = tk.Tk()
root.title("User Database")

show_db_button = tk.Button(root, text="Show Database", command=show_db_window)
show_db_button.pack()

add_user_button = tk.Button(root, text="Add User", command=add_user_window)
add_user_button.pack()

change_name_button = tk.Button(root, text="Change Name", command=change_name_window)
change_name_button.pack()

change_password_button = tk.Button(root, text="Change Password", command=change_password_window)
change_password_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

root.mainloop()
