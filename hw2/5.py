mon = str(input('Input the name of Month:'))
list_of_months = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for i in list_of_months:
    if i == mon:
        if i == "January" or i == 'March' or i =='May' or i =='July' or i == 'August' or i =='October' or i == 'December':
            print(31, "days")
        elif i == 'April' or i == 'June' or i == 'September' or i =='November':
            print(30, "days")
        else:
            print('28/29', "days")

