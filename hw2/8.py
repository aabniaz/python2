print("Input lengths of the triangle sides:")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x != y and x != z and y != z:
    print("Scalene triangle")
else:
    print("Isosceles triangle")
