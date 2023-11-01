listt = list(input().split(','))
occur = {}
for char in listt:
	if char in occur:
		occur[char] += 1
	else:
		occur[char] = 1
max_char = max(occur, key=occur.get)
print(f'he Most Frequent Element is:  {(max_char)}')