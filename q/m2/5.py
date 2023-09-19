#????
n = int(input())
sum = 0
last_num = 1
for i in range(1, n + 1):
    factor = 1
    i = last_num
    for j in range(i, 2 * i + 1):
        factor *= j
        last_num = j
    sum += factor
print(sum)