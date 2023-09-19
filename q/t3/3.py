def findall(string):
    l = []
    for i in range(len(string)):
        if string[i] == 'a': l.append(i)
    return l
print(findall(input()))