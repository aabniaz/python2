
#1
x = 2
print(type(x))

#2
string = "Hello"
print(len(string))

#5
items = [1,2,3,4,5,6,7,8]
print(sum(items))

#3
"""
x = input()
if type(x) is list:
    print('x is  list')
elif type(x) is tuple:
    print('x is tuple')
else: 
    print('x is set')
  """ 
  
#4
n = int(input())
list = [1,2 ,3, 4, -3, -5]
for i in list:
    while i >= 0:
        sum = (n*(n+1)/2)
        break
print(sum)

#6 
x, y = 4, 3
result = x * x + 2 * x * y + y * y
print(result)

""""#8 
import math
x1,y1,r1,x2,y2,r2 = int(input())
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d <= r1-r2:
    print("C2  is in C1")
elif :
    print("C1  is in C2")
elif :
    print("Circumference of C1  and C2  intersect")
else:
    print("C1 and C2  do not overlap")"""
