a = [1,[2,3],9,7,[4,5],'deepak']
count = 0
for i in a:
     if type(a) == type(i):
         count = 1
         print(type(i),)
         break
           
print('Loop Over')
if count == 1:
    print('Sub List Found:',i)
else:
    print('No Sublist Found')    