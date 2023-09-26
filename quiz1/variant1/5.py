"""num = input()
x1, y1, x2, y2 = map(int, input().split())
x1_1, y1_1, x2_2, y2_2 = map(int, input().split())
def find_a_and_b(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return a, b
a, b = find_a_and_b(x1, y1, x2, y2)
print(int(a),int(b))

def find_a1_and_b1(x1_1, y1_1, x2_2, y2_2):
    a1 = (y1_1 - y2_2) / (x1_1 - x2_2)
    b1 = y1_1- a * x1_1
    return a1, b1
a1, b1 = find_a_and_b(x1_1, y1_1, x2_2, y2_2)
print(int(a1),int(b1))
"""

num = int(input())
for i in range(num):
    x1, y1, x2, y2 = map(int, input().split())
    a, b = (y1 - y2) / (x1 - x2), y1 - ((y1 - y2) / (x1 - x2)) * x1
    print(f'({int(a)}, {int(b)})')