s = input()
s_len = len(s)
s_l = []
s_l.append(s[s_len-1])
s_l.append(s[0:s_len-1])
for i in s_l:
    print(i, end = '')
