d = True
number = int(input("Your number "))
while(d):
    n = int(input("Guess "))
    if n > number:
        print('the numver is fewer')
    elif n < number:
        print('the number is more')
    elif n == number:
        print("BINGO!")
        d = False
    

"""import random
n = random.randint(1, 100)
print(f"Number: {n}")
for i in range(3):
    guess = int(input("Guess: "))
    if guess == n: 
        print("BINGO!")
        break
    print("The number is fewer") if abs(n - guess) <= 25 else print("The number is more")
else: print("You lose. Try again!")"""