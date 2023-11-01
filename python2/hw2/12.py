n_1 = int(input('Input first number: '))
n_2 = int(input('Input second number: '))
n_3 = int(input('Input third number: '))

l = []
l.append(n_1)
l.append(n_2)
l.append(n_3)
l_s = sorted(l)
print('The median is', int(l_s[1]))