import math
n, r = map(int, input().split())

"""for i in range(n):
    x, y = map(int, input().split())
    l =math.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1]**2)"""
    
x0, y0 = 0, 0
x1, y1 = 2, 0
x2, y2 = 2, 2
x3, y3 = 0, 2

l1 = math.sqrt((x1-x0)**2+(y1-y0)**2)
l2 = math.sqrt((x2-x1)**2+(y2-y1)**2)
l3 = math.sqrt((x3-x2)**2+(y3-y2)**2)
l4 = math.sqrt((x3-x0)**2+(y3-y0)**2)

l = (l1+l2+l3+l4)
radius = 2*math.pi*r
print(l+radius)
