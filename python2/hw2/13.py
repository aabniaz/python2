yeart = int(input('Input a year: '))
montht = int(input('Input a month [1-12]: '))
dayt = int(input('Input a day [1-31]: '))
yeart_new = yeart

while yeart >= 4:
            yeart -= 4
if dayt == 29 and yeart == 0 and montht == 2:
            print(yeart_new,'-',montht,'-',1)
if dayt == 28 and yeart != 0 and montht == 2:
            print(yeart_new,'-',montht,'-',1)
if dayt == 31:
    if montht == 1 or montht == 3 or montht == 5 or montht == 7 or montht == 8 or montht ==10 or montht == 12:
                print(yeart_new,'-',montht,'-',1)
if dayt == 30:
    if montht == 4 or montht == 6 or montht == 9 or montht == 11:
                print(yeart_new,'-',montht,'-',1)
else:
        print('The next date is', yeart_new,'-',montht,'-',dayt + 1)
