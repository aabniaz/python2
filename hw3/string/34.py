s = input() 
count = {} 
for c in s: 
    if c in count: 
        count[c] += 1 
    else: 
        count[c] = 1 
 
for c in s: 
    if count[c] == 1: 
        result = c 
        break 
    else: 
        result = None 
 
if result is not None: 
    print(f"first non-repeating character: {result}") 
else: 
    print("there is no non-repeating char")
