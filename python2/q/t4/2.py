n = int(input())
n_new = []
#n=341
n1 = int(n / 100)
n2 = int((n%100) / 10)
n3 = int((n%10) % 10)

n_new.append(n3)
n_new.append(n2)
n_new.append(n1)
for i in n_new:
    print(i, end='')
