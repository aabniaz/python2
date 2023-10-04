def triangle(a, b, c):
    third_side = c ** 2
    first_second_side = a ** 2 + b ** 2
    if third_side == first_second_side:
        return 'R'  # Right triangle    
    elif third_side < first_second_side:
        return 'A'  # Acute triangle
    else:
        return 'O'  # Obtuse triangle
    
num_triangles = int(input().strip())
for _ in range(num_triangles):
    a, b, c = map(int, input().strip().split())
    name = triangle(a, b, c)
    print(name, end=' ')
print()
