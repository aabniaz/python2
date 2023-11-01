word = input()
vowel = 'aeiou'
prefix = ''
for letter in word:
    if letter not in vowel:
        prefix += letter
    else: 
        break

new_word = word[len(prefix):] + prefix.lower() + 'ay'
print(new_word)
