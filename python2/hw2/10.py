d = int(input("Input birthday:"))
mon = str(input('Input month of birth (e.g. march, july etc):'))

if mon == 'January' and d >= 21 or mon == 'February' and d <= 19:
        print("Your Astrological sign is :","Aquarius")
if mon == 'February' and d >= 20 or mon == 'March' and d <= 20:
    print("Your Astrological sign is :","Pisces")
if mon == 'March' and d >= 21 or mon == 'April' and d <=19:
    print("Your Astrological sign is :","Aries")
if mon == 'April' and d >=20 or mon == 'May' and d <= 20:
    print("Your Astrological sign is :","Taurus")
if mon == 'May' and d >= 21 or mon == 'June' and d <= 20:
    print("Your Astrological sign is :","Gemini")
if mon == 'June' and d >= 21 or mon == 'July' and d <= 22:
    print("Your Astrological sign is :","Cancer")
if mon == 'July' and d >= 23 or mon == 'August' and d <= 22:
    print("Your Astrological sign is :","Leo")
if mon == 'August' and d >= 23 or mon == 'September' and d <= 22:
    print("Your Astrological sign is :","Virgo")
if mon == 'September' and d >= 23 or mon == 'October' and d <= 23:
    print("Your Astrological sign is :","Libra")
if mon == 'October' and d >= 24 or mon == 'November' and d <= 22:
    print("Your Astrological sign is :","Scorpio")
if mon == 'November' and d >= 23 or mon == 'December' and d <= 21:
    print("Your Astrological sign is :","Sagittarius")
if mon == 'December' and d >= 22 or mon == 'January' and d <= 20:
    print("Your Astrological sign is :","Capricorn")