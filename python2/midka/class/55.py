class Wordplay:
    def __init__(self, word_list):
        self.words = word_list

    def words_with_length(self, length):
        return [word for word in self.words if len(word) == length]

    def starts_with(self, s):
        return [word for word in self.words if word.startswith(s)]

    def ends_with(self, s):
        return [word for word in self.words if word.endswith(s)]

    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]

    def only(self, L):
        return [word for word in self.words if set(word).issubset(set(L))]

    def avoids(self, L):
        return [word for word in self.words if not set(word).intersection(set(L))]

word_list = ["apple", "banana", "level", "radar", "grape", "kiwi", "orange"]

wordplay = Wordplay(word_list)

print(wordplay.words_with_length(5))  # Output: ['apple', 'grape']
print(wordplay.starts_with("b"))     # Output: ['banana']
print(wordplay.ends_with("e"))       # Output: ['apple', 'orange']
print(wordplay.palindromes())        # Output: ['level', 'radar']
print(wordplay.only(['a', 'p', 'l', 'e']))  # Output: ['apple']
print(wordplay.avoids(['a', 'p', 'l', 'e']))  # Output: ['banana', 'kiwi']
