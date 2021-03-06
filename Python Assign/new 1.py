a = 'best places to visit in the world '
b = 'to','in','the'
n = a
print('Before:',n)
for i in b:
  n = n.replace(i,"")
print('After:',n)  