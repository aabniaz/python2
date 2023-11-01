#????

def calculate_sum(n):
    result = 0
    product = 1

    for i in range(1, n + 1):
        product *= i
        result += i * product

    return result

n = 2 

total_sum = calculate_sum(n)

print(f"The sum for n = {n} is {total_sum}")
