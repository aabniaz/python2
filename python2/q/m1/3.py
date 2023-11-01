for i in range(100, 999):
    first = int(i//100)
    second = int((i//10)%10)
    third = int(i%10)
    if first**3 + second**3 +  third**3 == i:
        print(i)



"""
def is_sum_of_cubes_of_digits_equal_to_number(number):
    # Extract individual digits
    hundreds_digit = number // 100
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

    # Calculate the sum of cubes of the digits
    sum_of_cubes = (hundreds_digit ** 3) + (tens_digit ** 3) + (ones_digit ** 3)

    # Check if the sum of cubes equals the original number
    return sum_of_cubes == number

def find_numbers_with_sum_of_cubes_equal_to_number():
    valid_numbers = []

    # Iterate through all three-digit numbers
    for number in range(100, 1000):
        if is_sum_of_cubes_of_digits_equal_to_number(number):
            valid_numbers.append(number)

    return valid_numbers

# Find three-digit numbers with the sum of cubes of digits equal to the number
valid_numbers = find_numbers_with_sum_of_cubes_equal_to_number()

print("Three-digit numbers with sum of cubes of digits equal to the number:")
print(valid_numbers)"""
