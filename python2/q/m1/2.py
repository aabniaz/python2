"""def ascnumber(integer):
    first = integer // 100
    second =  (integer // 10) % 10
    third = integer % 10
    return first <= second <= third

number = 123

ascnumber = ascnumber(number)

if ascnumber:
    print(f"the digits in {number} are arranged in asc order")
else:
    print(f"the digits in {number} are not arranged in asc order")"""

n = int(input())
first = int(n // 100)
second = int((n // 10) % 10)
third = int(n % 10)

if first < second and second < third:
    print("yes")
else:
    print("no")