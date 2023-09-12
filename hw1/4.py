import sys
import math
#1
print(f"Python version: {sys.version}")

#2
x = int(input())
second_side = 2 * x
rect_area = x * second_side 
print(f'rect area is {rect_area}')

#3
firstname = input()
lastname = input()
print(lastname + " " + firstname)

#5
mylist = ["apple", "banana", "blueberry", "strawberry"]
print(mylist[0])
print(mylist[-1])

#6
n = int(input())
nn = n * n
nnn = n ** 3
print(n + nn + nnn)

#7
radius = 8
sphere_volume = (4/3) * math.pi * (radius ** 3)
print(sphere_volume)

#8
def test(n):
  return ((abs(n - 1000) <= 100) or (abs(n - 2000) <= 100))
print(test(800))
print(test(1100))

#9
values = [1, 5, 8, 3]
s_value = int(input())
if s_value in values:
    print("True")
else: print("False")

#10
base = int(input())
height = int(input())
tr_area = (1/2) * base * height
print(f"triangular area is {tr_area}")

#11
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(dist)

#12
a = 5
b = 8
c = 6
d = 7
e = 9
f = 4
y = 22 // 11
x_1 = (6 - 8 * y)/5
x_2 = (4 - 9 * y)/7
x_1 = x_2

print(f"y: {y}")
x = (6 - 8 * y)/5
print(f"x: {x}")





