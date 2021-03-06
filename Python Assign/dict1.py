a = "deepika, stupid but smart,smart but stupid."
#a = a.split()
print(a)
d = {}
for i in a:
    if i == ' ' or i == ',' or i == '.':
        continue
    elif i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)