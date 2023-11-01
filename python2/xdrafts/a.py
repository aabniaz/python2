#1
numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print (','.join(numbers))

#2 
print('enter celsius:')
c = float(input())
f = (c * 9/5) + 32
print(f'fahrenheit: {f}')
print('enter fahrenheit:')
f1 = float(input())
c1 = (f1 - 32) * (5/9)
print(f'celsius: {c1}')

#3
import random
num, guess_num = random.randint(1, 10), 0
while num != guess_num:
    guess_num = int(input("Guess it correct!: "))
print('Well guessed!')

#4
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
for j in range(1, rows + 1):    
    for i in range(1, i):
        print("*", end=" ")
    print('')

#5
word = str(input())
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")




"""#6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for x in numbers:
    if not x % 2:
    	     even+=1
    else:
    	     odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
"""
"""number = 5
while a != number:
    for a in range(1,10):
        print(input('enter a guess'))
        break
    if a == number:
        break
print("yess")"""
