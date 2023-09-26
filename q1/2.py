word = input()
vowel = 'aeiou'
prefix = ''
for letter in word:
    if letter[0] in vowel:
        new_word = word + 'yay'
        print(word + ' -> ' + new_word)
        break
    else: 
        print('the first char is not a vowel')
        break


