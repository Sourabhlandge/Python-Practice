# a = '''1,2,3,4
# 4,5,6,5
# 7,8,9,6
# 1,1,1,1'''
# s = [i for i in (x.split(",") for x in a.split("\n"))]
# print(s)
    
              
L = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]] 
          
# Printing list of list 
print("Initial List - ", str(L)) 
  
# Using naive method 
res = list() 
for j in range(0, len(L[0])): 
    tmp = 0
    for i in range(0, len(L)): 
        tmp = tmp + L[i][j] 
    res.append(tmp) 
      
# printing result 
print("final list - ", str(res)) 
