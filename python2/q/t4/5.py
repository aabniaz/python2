#????
word = input()
encoded_word = input()
def isEncoded(word, encoded_word): 
    dict = {}
    for i in range(len(word)):
        for j in range(len(encoded_word)):
            if i == j:
                if word[i] not in dict.keys(): 
                    if word[i] == encoded_word[j]: return False
                    dict[word[i]] = encoded_word[j]
                else: 
                    if encoded_word[j] != dict[word[i]]: return False
    return True
print(isEncoded(word, encoded_word))


"""
def is_encoded_version(original_str, encoded_str):
    if len(original_str) != len(encoded_str):
        return False

    mapping = {}  # Dictionary to store the mapping of characters

    for i in range(len(original_str)):
        original_char = original_str[i]
        encoded_char = encoded_str[i]

        if original_char in mapping:
            if mapping[original_char] != encoded_char:
                return False
        else:
            if encoded_char in mapping.values():
                return False
            mapping[original_char] = encoded_char

    return True

# Example usage
original_str = input("Enter the original string: ").upper()
encoded_str = input("Enter the encoded string: ").upper()

if is_encoded_version(original_str, encoded_str):
    print(f"'{encoded_str}' could be an encoded version of '{original_str}'.")
else:
    print(f"'{encoded_str}' is not an encoded version of '{original_str}'.")
"""