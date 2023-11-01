#?
"""s = input()
q = ''
for c in s:
    if c not in q:
        s_c = s.count(c)
        print(c,':', s_c)
        q += c"""

word = input()
letters = list(set(word))
letters.sort()
for ch in letters:
    print(f"{ch}: {word.count(ch)}")