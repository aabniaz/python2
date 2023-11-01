"""a = [1, 1, 2, 3, 5, 8, 13, 13, 34, 55, 89]
b = set(list(a))
print(b)"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
def nodubl():
    for element in a:
        if element not in b:
            b.append(element)
    print(b)
nodubl()
