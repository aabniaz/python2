strr = input()
occur = {}
for char in strr:
	if char in occur:
		occur[char] += 1
	else:
		occur[char] = 1
max_char = max(occur, key=occur.get)
print(f'The maximum of all characters in {strr} is:  {str(max_char)}')
