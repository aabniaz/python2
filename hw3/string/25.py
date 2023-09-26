number = input()
number = number.replace(',', '')
formatted_number = '{:,}'.format(int(number))
print(formatted_number)
