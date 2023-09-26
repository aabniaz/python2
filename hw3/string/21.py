filename = 'text.txt'
prefix = 'prefix '

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    prefixed_line = prefix + line.strip()
    print(prefixed_line)
