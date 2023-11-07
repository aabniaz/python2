import tkinter as tk
import re
import json
import mysql.connector as mysql

def connect_to_db():
    conn = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "15082004Aa@"
    )
    
    cursor = conn.cursor()
    return conn, cursor
    # return db

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

# def add_user_db(name, password):
#     db = load_from_txt()
#     while name in db.keys():
#         name = input('Please choose another name: ')
#     if check_password(password):
#         db[name] = password
#         save_to_txt(db)
#         print(f'User {name} added successfully.')

def add_user_db(name, password):
    print(name, password)
    query = "select name from users"
    print(f"insert into users values('{name}', '{password}')")
    cursor.execute(query)
    names = cursor.fetchall()
    print(names)
    names = list(map(lambda x: x[0], names))
    print(names)
    
    if name in names:
        print("already exists")
    else:
        cursor.execute(f"insert into users values('{name}', '{password}')")
        
    cursor.execute(query)
    print(cursor.fetchall())
    
    db = load_from_txt()
    while name in db.keys():
        name = input('Please choose another name: ')
    if check_password(password):
        db[name] = password
        save_to_txt(db)
        print(f'User {name} added successfully.')
    
    conn.commit()

# def change_name_db(old_name, new_name, password):
#     db = load_from_txt()
#     while password != db[old_name]:
#         password = input('Wrong password! Try again: ')

#     db[new_name] = db.pop(old_name)
#     save_to_txt(db)

# def change_password_db(name, old_password, new_password):
#     db = load_from_txt()
#     if name in db:
#         while old_password != db[name]:
#             old_password = input('Wrong password! Try again: ')

#         if check_password(new_password):
#             db[name] = new_password
#             save_to_txt(db)
#             print(f'Password for user {name} changed successfully.')
#     else:
#         print(f'User {name} does not exist in the database.')

def change_name_db(old_name, new_name, password):
    query = "select name, password from users"
    cursor.execute(query)
    user_data = cursor.fetchall()
    user_dict = {name: pwd for name, pwd in user_data}

    if old_name in user_dict:
        if password == user_dict[old_name]:
            if new_name not in user_dict:
                update_query = f"update users set name = '{new_name}' where name = '{old_name}'"
                cursor.execute(update_query)
                conn.commit()

                print(f"User name updated from {old_name} to {new_name}.")
            else:
                print("The new name already exists.")
        else:
            print("Incorrect password.")
    else:
        print("User not found in the database.")

def change_password_db(name, old_password, new_password):
    query = f"select password from users where name = '{name}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        current_password = result[0]

        if old_password == current_password:
            if check_password(new_password):
                update_query = f"update users set password = '{new_password}' where name = '{name}'"
                cursor.execute(update_query)
                conn.commit()

                print(f"Password for user {name} changed successfully.")
            else:
                print("New password does not meet the criteria.")
        else:
            print("Incorrect old password.")
    else:
        print(f"User {name} does not exist in the database.")


def add_user_window():
    add_user_window = tk.Toplevel(root)
    add_user_window.title("Add User")

    add_name_label = tk.Label(add_user_window, text="New User Name:")
    add_name_label.pack()
    add_name_entry = tk.Entry(add_user_window)
    add_name_entry.pack()

    add_password_label = tk.Label(add_user_window, text="New User Password:")
    add_password_label.pack()
    add_password_entry = tk.Entry(add_user_window)
    add_password_entry.pack()

    add_user_button = tk.Button(add_user_window, text="Add User", command=lambda: add_user_db(add_name_entry.get(), add_password_entry.get()))
    add_user_button.pack()

    exit_button = tk.Button(add_user_window, text="Exit", command=add_user_window.destroy)
    exit_button.pack()

def change_name_window():
    change_name_window = tk.Toplevel(root)
    change_name_window.title("Change Name")

    old_name_label = tk.Label(change_name_window, text="Old User Name:")
    old_name_label.pack()
    old_name_entry = tk.Entry(change_name_window)
    old_name_entry.pack()

    new_name_label = tk.Label(change_name_window, text="New User Name:")
    new_name_label.pack()
    new_name_entry = tk.Entry(change_name_window)
    new_name_entry.pack()

    change_name_password_label = tk.Label(change_name_window, text="Password:")
    change_name_password_label.pack()
    change_name_password_entry = tk.Entry(change_name_window)
    change_name_password_entry.pack()

    change_name_button = tk.Button(change_name_window, text="Change Name", command=lambda: change_name_db(old_name_entry.get(), new_name_entry.get(), change_name_password_entry.get()))
    change_name_button.pack()

    exit_button = tk.Button(change_name_window, text="Exit", command=change_name_window.destroy)
    exit_button.pack()

def change_password_window():
    change_password_window = tk.Toplevel(root)
    change_password_window.title("Change Password")

    change_password_name_label = tk.Label(change_password_window, text="User Name:")
    change_password_name_label.pack()
    change_password_name_entry = tk.Entry(change_password_window)
    change_password_name_entry.pack()

    old_password_label = tk.Label(change_password_window, text="Old Password:")
    old_password_label.pack()
    old_password_entry = tk.Entry(change_password_window)
    old_password_entry.pack()

    new_password_label = tk.Label(change_password_window, text="New Password:")
    new_password_label.pack()
    new_password_entry = tk.Entry(change_password_window)
    new_password_entry.pack()
    change_password_button = tk.Button(change_password_window, text="Change Password", command=lambda: change_password_db(change_password_name_entry.get(), old_password_entry.get(), new_password_entry.get()))
    change_password_button.pack()

    exit_button = tk.Button(change_password_window, text="Exit", command=change_password_window.destroy)
    exit_button.pack()

def show_db_window():
    sql_query = "select * from users"
    cursor.execute(sql_query)
    records = cursor.fetchall()
    print(records)
    
    show_db_window = tk.Toplevel(root)
    show_db_window.title("Show Database")

    db_display = tk.Text(show_db_window, height=10, width=50)
    db_display.pack()

    for name, password in records:
        db_display.insert(tk.END, f'{name}: {password}\n')

def main_window():
    welcome_label = tk.Label(root, text="Welcome to the user's database!")
    welcome_label.pack()

    action_label = tk.Label(root, text="What would you like to do?")
    action_label.pack()

    show_db_button = tk.Button(root, text="Show Database", command=show_db_window)
    show_db_button.pack(pady=10)

    add_user_button = tk.Button(root, text="Add User", command=add_user_window)
    add_user_button.pack(pady=10)

    change_name_button = tk.Button(root, text="Change Name", command=change_name_window)
    change_name_button.pack(pady=10)

    change_password_button = tk.Button(root, text="Change Password", command=change_password_window)
    change_password_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

conn = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "15082004Aa@"
)

cursor = conn.cursor()
cursor.execute("use test")

root = tk.Tk()
root.title("User Database")
root.geometry("400x300")  
root.configure(bg='#03B3C8')
main_window()
root.mainloop()

