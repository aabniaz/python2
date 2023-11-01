def collatz_seq(x):
    steps = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        steps += 1
    return steps

num = int(input().strip())
test_cases = list(map(int, input().strip().split()))
steps_list = [collatz_seq(x) for x in test_cases]
print(' '.join(map(str, steps_list)))
