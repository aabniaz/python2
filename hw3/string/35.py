s = str(input()) 
count = {} 
for c in s: 
    if c in count: 
        result = c 
        break 
    else: 
        count[c] = 1 
 
if 'result' in locals(): 
    print(f"first repeated character: {result}") 
else: 
    print("there is no repeated char")
