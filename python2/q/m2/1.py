"""a = int(input())
b = int(input())
h = (a**2 + b**2)**0.5
s = (a * b) / 2
p = a + b + h
print("hypotenuse:", h)
print("area:", s)
print("perimeter:", p)"""

"""a,b = map(int,input().split())
c = ((a**2)+(b**2))**0.5
P = a+b+c
S = (a*b)/2
print(c,P,S)"""

a,b = map(int, input().split())
c = ((a**2+b**2)**0.5)
P = a+b+c
S = (a*b)/2
print(c,P,S)
