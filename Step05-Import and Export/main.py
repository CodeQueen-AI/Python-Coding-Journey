import index
result = index.add(5, 3)
print(result) 

#Import Specific Function
from index import add
print(add(10, 5)) 

# Importing with an Alias
import index as m
print(m.multiply(4, 2)) 

#Import Everything
from index import *
print(add(6, 4)) 
print(multiply(3, 3))  
