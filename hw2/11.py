import datetime
x = datetime.datetime.now()
cur_year = x.year
b_y = int(input("Input your birth year: "))

chan = cur_year - b_y
while chan > 12:
    chan -= 12

if chan == 1 or chan ==-11:
    print('Your Zodiac sign: ','Ox')
elif chan ==2 or chan ==-10:
    print('Your Zodiac sign: ','Rat')
elif chan == 3 or chan ==-9:
    print('Your Zodiac sign: ','Pig')
elif chan == 4 or chan ==-8:
    print('Your Zodiac sign: ','Dog')
elif chan == 5 or chan ==-7:
    print('Your Zodiac sign: ','Rooster')
elif chan == 6 or chan ==-6:
    print('Your Zodiac sign: ','Monkey')
elif chan == 7 or chan ==-5:
    print('Your Zodiac sign: ','Goat')
elif chan == 8 or chan ==-4:
    print('Your Zodiac sign: ','Horse')
elif chan == 9 or chan ==-3:
    print('Your Zodiac sign: ','Snake')
elif chan ==10 or chan ==-2:
    print('Your Zodiac sign: ','Dragon')
elif chan ==11 or chan ==-1:
    print('Your Zodiac sign: ','Rabbit')
elif chan ==12 or chan ==-12 or chan ==0:
    print('Your Zodiac sign: ','Tiger')