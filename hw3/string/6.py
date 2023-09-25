a = input()
try:
    if a[-3:] != 'ing':
        print(a + 'ing')

except:
    print('length is less than 3')
else:
    if a[-3:] == 'ing':
        print(a + 'ly')