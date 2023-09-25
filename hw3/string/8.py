def length(a):
    longest_length = 0
    for word in a:
        word_length = len(word)
        if word_length > longest_length:
            longest_length = word_length
    return longest_length
try:
    a = ['apple', 'mango', 'banana', 'strawberry']
    print("Length of the longest word:", length(a))
except TypeError as te:
    print(f"Error: {te}")
