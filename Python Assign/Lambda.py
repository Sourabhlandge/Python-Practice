def fun(x):
	print('o/p from def function:',x)
fun(10)
print('----------------------------------------------')
fun=lambda x:x+1
print('o/p from lambda function:',fun(10))

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#new program
def fun(x,y):
	print('o/p from def function:',x+y)
fun(10,20)
print('----------------------------------------------')
fun=lambda x,y:x+y
print('o/p from lambda function:',fun(10,20))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#new program

fun=lambda x,y: 'deepak' if x == 10 else 'sachin'
print(fun(10,20))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#Assignment #convert below to lambda

# def fun(a):
	# if a==10:
		# print('got ten')
	# elif a==20:
		# print('got twenty')
	# else:
		# print('waste')

# fun(20)
#new
#assignments , what is the output ? #syntax Error Occure
# def heloo(deepak):
	# print('This is Maze',deepak)
# def deepak(xyz,pqr)
	# xyz(pqr)
		
# deepak(heloo,deepak)

