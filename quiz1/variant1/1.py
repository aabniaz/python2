l1 = 'message' #l1 = input()
l1_new =  []
l2_new = []
for i in range(0, len(l1)):
    if i % 2 == 0:
       l1_new.append(l1[i]) 
    if i % 2 != 0:
        l2_new.append(l1[i]) 
for x in (l1_new + l2_new):
    print(x, end='')