import random
word_list = ["GRAVITY", "FORCE", "PRESSURE", "RELATIVITY", "VISCOSITY"]

def display_word(word, guessed_letters):
    my_word = ""
    for letter in word:
        if letter in guessed_letters:
            my_word += letter + " "
        else:
            my_word += "_ "
    return my_word.strip()

def hangman():
    random_word = random.choice(word_list).upper()  # to choose a random word from the list
    guessed_letters = set()
    print("Welcome to Hangman!")
    print(display_word(random_word, guessed_letters))
    while True:
        guess = input("Guess your letter: ").upper()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        if guess not in random_word:
            print("Incorrect!")
        else:
            print("Correct guess!")
        my_word = display_word(random_word, guessed_letters)
        print(my_word)

        if "_" not in my_word:
            print("Congratulations! You guessed the word.")
            break
hangman()

"""place = "123456789" 
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
"""
