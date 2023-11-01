place = "123456789"
while(place != "EVAPORATE"):
    s = input("Guess your letter: ")
    if s == "E":
        place = place.replace(place[0], "E")
        place = place.replace(place[8], "E")
        print(place)
    elif s == "V":
        place = place.replace(place[1], "V")
        print(place)
    elif s == "A":
        place = place.replace(place[2], "A")
        place = place.replace(place[6], "A")
        print(place)
    elif s == "P":
        place = place.replace(place[3], "P")
        print(place)
    elif s == "O":
        place = place.replace(place[4], "O")
        print(place)
    elif s == "R":
        place = place.replace(place[5], "R")
        print(place)
    elif s == "T":
        place = place.replace(place[7], "T")
        print(place)
    else: print("Incorrect")
