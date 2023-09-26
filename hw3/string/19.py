string = input('string: ')
spec_char = input('specified characters: ')
if string[:len(spec_char)] == spec_char:
    print(f'the string starts with spec_char: {spec_char}')
else:
    print('no')