from collections import Counter 
  
reviews = '''I am regular customer of zomato, curry was very tasty
paneer tikka bahut hi tasty tha, nice
It is too spicy, but tasty
over_priced
nice
spicy, over_priced
yummy, nice'''
  
s = reviews.split() 
#print(s)
  
  
Counter = Counter(s) 
  
freq_reviews = Counter.most_common(4) 
  
print(freq_reviews) 