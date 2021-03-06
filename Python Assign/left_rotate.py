import array as arr
arr = arr.array('i',[1,2,3,4,5,6,7])
n = len(arr)
no_of_r = 1
print("Before r:")
for i in range(0,n):
     print(arr[i], end = ' ')
leftRotate(arr,no_of_r,n)
print("\nAfter R")
for i in range(0,n):
     print(arr[i],end = ' ')
