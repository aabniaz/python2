a,b,c = map(int, input().split())
d = int(b**2-4*a*c)
try:
    d_sq = int(d**0.5)
    if a == 0:
        x = -c/b
        print(x)
    else: 
        x1 = (-b + d_sq)/ (2*a)
        x2 = (-b - d_sq)/ (2*a)
        print(x1, x2)
except:
    print("no roots")


