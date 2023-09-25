a = input()
upp = sum(1 for char in a[:4] if char.isupper())
if upp >= 2:
    print(a.upper())
else:
    print('no')


