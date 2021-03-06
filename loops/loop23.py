no=int(input("Enter the value:"))
if no>1:
    for x in range(2,no):
        if(no%x)==0:
            print(no,"is not prime")
            break
        else:
            print(no,"is a prime")
else:
    print(no,"is not a prime")
