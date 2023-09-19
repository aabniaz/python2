up = int(input('up '))
down = int(input('down '))
left = int(input('left '))
right = int(input('right '))

x = 0
y = 0
y = y + up
y = y - down
x = x - left
x = x + right

print(int((x**2+y**2)**0.5))