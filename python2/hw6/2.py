def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
n = int(input())
fibonacci_n = fibonacci(n)
cubed = list(map(lambda x: x ** 3, fibonacci_n))
print(cubed)
