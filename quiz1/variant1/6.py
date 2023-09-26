l1 = [3,6,9,12,15,18,21]
l1_odd = []
l2 = [4,8,12,16,20,24,28]
l2_even = []
for i in range(0, len(l1)):
    if i % 2 != 0:
       l1_odd.append(l1[i]) 
for even in range(0, len(l2)):
    if even % 2 == 0:
        l2_even.append(l2[even])
print(l1_odd+l2_even)
