array_size = int(input().strip())
arr = input().split()
sorted_arr = sorted(arr)
initial_indices = []

for i in range(len(sorted_arr)):
    initial_indices.append(arr.index(sorted_arr[i]) + 1)

print(' '.join(map(str, initial_indices)))
