a = input()
if len(a) % 4 == 0:
    b = a[::-1]
    print(b)
else:
    print('length of input is not a multiple of 4')