str = input().split()
result = []
for word in str:
    if len(word) > 1:
        cap_words = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        cap_words = word.upper()
    result.append(cap_words)
print(' '.join(result))