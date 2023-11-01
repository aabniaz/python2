global db
db = {'Ali': 'ali', 'Alua': 'alua', 'Jandaulet': 'jandaulet'}


def show_db():
    print(db)


def change_name(old_name, new_name, password):
    while password != db[old_name]:
        password = input('Wrong password! Try again: ')

    db[new_name] = db[old_name]


def add_user(name, password):
    while name in db.keys():
        name = input('Please choose another name: ')
    if check_password(password):
        db[name] = password
        print(f'user {name} added successfully')
        show_db()
    else:
        print(f'User doesnt changed.')
   




def check_password(password):
    count = 0
    #[A-Z], [a-z], @#$%^%, len >6, [0-9]
    while count != 2:
        if len(password) >= 6:
            count = count + 1
        elif '@' or '#' in password:
            count = count + 1
        else:
            password = input('Enter another password: ')

    return True


print("Welcome to the users database!")
action = input("What would you like to do? (show db/add User/change Name/change Password): ")

if action == 'show db':
    show_db()
elif action == 'add User':
    name = input('Enter name: ')
    password = input('Enter password: ')
    add_user(name, password)
elif action == 'change Name':
    old_name = input('Enter the old name: ')
    new_name = input('Enter the new name: ')
    password = input('Enter password: ')
    change_name(old_name, new_name, password)
