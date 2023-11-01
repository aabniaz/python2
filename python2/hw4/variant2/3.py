def phone_end_eight(data):
    print("Users whose phone number ends in 8:")
    for user in data:
        if user['phone'].endswith('8'):
            print(user['name'])

def no_email(data):
    print("Users that don't have an email address:")
    for user in data:
        if not user['email']:
            print(user['name'])

data = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
        {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
        {'name': 'Princess', 'phone': '555-3141', 'email': ''},
        {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]

phone_end_eight(data)
no_email(data)
