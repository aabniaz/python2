def replace_not_poor(a): 
    noot = a.find('not')
    poor = a.find('poor')
    if noot != -1 and poor != -1 and noot < poor:
        return a[:noot] + 'good' + a[poor + 4:]
    else:
        return a
try:
    a = input()
    result = replace_not_poor(a)
    print("Modified string:", result)
except TypeError as te:
    print(f"Error: {te}")
