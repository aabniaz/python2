"""def power(m):
    return m ** m
m = int(input())
print(power(m))"""

def power(m, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(m, n)
    else:
        result = 1
        for _ in range(n):
            result *= m
        return result

m1, n1 = map(int, input().split())
print(power(m1,n1))