"""strr = 'home'
strr_new = []
strr_new.append(strr[-1])
strr_new.append(strr[0])
strr_new.append(strr[1])
strr_new.append(strr[2])
for i in strr_new:
    print(i, end='')
"""

n = input('enter int or str: ')
n_new = n[-1]+n[:-1]
print('result:', n_new)
