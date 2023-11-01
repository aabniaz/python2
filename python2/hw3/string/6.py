a = input()
try:
    if len(a) < 3:
        raise ValueError('length is less than 3')
except ValueError as e:
    print('error:', str(e))
else:
    if a[-3:] == 'ing':
        print(a + 'ly')
    else:
        print(a + 'ing')
