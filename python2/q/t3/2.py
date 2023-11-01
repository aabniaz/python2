n = int(input())
if n // 1000 == n % 10 and (n // 100) % 10 == (n % 100) // 10:
    print("Yes") 
else: print("No")