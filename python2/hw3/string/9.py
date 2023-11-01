s = str(input()) 
n = int(input()) 
try: 
    s= s.replace(s[n],'') 
    print(s) 
except: 
    if n > len(s): 
        print("Out of range")
