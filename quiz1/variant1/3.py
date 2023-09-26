"""L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
for x in L:
    if x[0] == 'a' and x[3] == 'a':
        print(x)"""

L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
my_dict = {1: 'a', 4: 'a'} 
strr = []
for i, string in enumerate(L, start=1):
    match = True
    for index, char in my_dict.items():
        if len(string) < index or string[index - 1] != char:
            match = False
            break
    if match:
        strr.append(i)
print(strr)

