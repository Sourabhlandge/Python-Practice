def fun1(a,b):
	print('This is function one and addition of a and b is:',a+b)
	if a==10:
		return 'ten'
	else:
		return 'not a good value'

#fun1() simple calling function,not callable bcoz fun1 take 2 parameter and here not pass any parameter

x=fun1(20,30) # calling a funciton with parameter
print(x)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")



#new program

def fun(a=0,b=0):
	print('value of a is ',a)
	print('value of b is ',b)#o/p zero bcoz b = 0 and a=10 bcoz parameter pass
fun(10)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


#new program
def fun(**args):
	print('args',args)
	
fun(a=10,b=20,c=30)#multiple values can assign in the form of dictionary