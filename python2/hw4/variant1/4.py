filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
strr = lines[0].strip()
first_name = strr[0:3]
last_name = strr[4:10]
phone_number = strr[-8:-1]
first_n = first_name[0].upper() + first_name[1:]
last_n = last_name[0].upper() + last_name[1:]
phone_n = '301-' + phone_number[0:]
result = first_n + ' ' + last_n + ' ' + strr[11:-9] + ' ' + phone_n
with open('output.txt', 'w') as file:
    file.write(result)
