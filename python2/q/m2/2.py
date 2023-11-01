"""x,y = map(int,input().split())
result = (x-y)**0.5
if result > 0:
    print(result)
else: print("plz enter valid numbers")"""

import math
x = int(input('x = '))
y  = int(input('y = '))

try:
    s = math.sqrt(x-y)
    s_1 = round(s, 3)
    print("Output: ", s_1)
except:
    print("plz enter valid numbers")