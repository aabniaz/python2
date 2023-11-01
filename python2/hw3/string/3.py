a = input()
b = []
try:
    a1 = a[0] + a[1] + a[-2] + a[-1]
except IndexError:
    print('string index out of range')
except TypeError:
    print('TypeError')
else:
    print(a1)
    
