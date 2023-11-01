alphabet = input("Enter an alphabet: ")
def for_vowel(alphabet):
    alphabet = alphabet.lower()
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
result = for_vowel(alphabet)
print(result)
