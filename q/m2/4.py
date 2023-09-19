"""import re
passwords = input().split(",")
for password in passwords:
    if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password) and 6 <= len(password) <= 12: 
        print(password)"""

import re
password = list(input().split(','))
empty = []
for w in password:
    x = re.findall("[a-zA-Z]", w)
    y = re.findall("[0-9]", w)
    z = re.findall("[$#@]", w)
    if x != empty and y != empty and z != empty and len(w) >= 6 and len(w) <= 12:
        print(w)