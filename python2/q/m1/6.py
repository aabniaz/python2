#???
s2,s1 = map(str,input('ana_str_str :').split())
a = sorted(s1)
b = sorted(s2)

s1_r =  s1.replace(s1[0],'')
s1_r1 =  s1.replace(s1[len(s1)-1],'')
a1 = sorted(s1_r)
a2 = sorted(s1_r1)
if a1 == b or b == a2:
    print(s2,s1, '--->', 'True')
else:
    print(s2,s1,'--->',"False")