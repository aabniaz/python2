def arithm_seq(A, B, N):
    return N * (2 * A + (N - 1) * B) // 2

num = int(input().strip())

for _ in range(num):
    A, B, N = map(int, input().split())
    summ = arithm_seq(A, B, N)
    print(summ, end=' ')
print() 
