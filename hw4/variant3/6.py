def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

number = int(input().strip())

for _ in range(number):
    x1, y1, x2, y2, x3, y3 = map(float, input().strip().split())
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    print(f'{area}', end=' ')

