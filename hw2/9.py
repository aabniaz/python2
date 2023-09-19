month = int(input('Input a month [1-12]: '))
day = int(input('Input a day [1-31]: '))
list_of_months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if month == 1 or month == 2 or month == 12:
    a = 'winter'
elif month ==4 or month ==5 or month == 3:
    a = 'spring'
elif month == 7 or month == 8 or month ==6:
    a = 'summer'
else:
    a = 'autumn'
print(list_of_months[month-1], ',', day, '.', 'Season is', a)
