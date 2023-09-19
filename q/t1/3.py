def findall(string):
    l = []
    for i in range(len(string)):
        if string[i] == 'a': l.append(i)
    return l
print(findall(input()))


"""def findall(s, character):
    positions = []
    for i in range(len(s)):
        if s[i] == character:
            positions.append(i)
    return positions

# Example usage
string = "banana"
char_to_find = 'a'
result = findall(string, char_to_find)
print(f"Positions of '{char_to_find}' in '{string}': {result}")"""

