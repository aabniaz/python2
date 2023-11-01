filename = 'input.txt'
with open(filename, 'r') as file:
    words = file.read().split()
for word in words:
     max_length = len(word)
     if len(word) == max_length:
        longest_words = word
with open('output.txt', 'w') as file:
    file.write(longest_words)
print("Longest word has been written to", 'output.txt')
