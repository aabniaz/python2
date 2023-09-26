a = input()
if len(a) < 2:
    print("string must have at least 2 chars")
b = a[-2:]    
c = b * 4
print(a, '->', c)
