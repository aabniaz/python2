str = input('string: ')
n_input = input('n of lowercases: ')
n = int(n_input)
result = str[:n].lower() + str[n:]
print("String with first", n, "characters in lowercase:", result)
