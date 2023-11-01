import collections
a = 'thequickbrownfoxjumpsoverthelazydog'
b = collections.defaultdict(int)
for i in a:
    b[i] += 1
    for i in sorted(b, key=b.get, reverse=True):
        if b[i] > 1:
            print('%s %d' % (i, b[i]))
