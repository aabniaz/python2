str = input()
result = ''
for char in str:
    if char == ',':
        result += '.'
    elif char == '.':
        result += ','
    else:
        result += char
print(result)
