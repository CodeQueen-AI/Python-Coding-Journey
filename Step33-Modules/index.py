#Importing a Built-in Module
import math  
print(math.sqrt(25))  

#Importing Specific Functions from a Module
from math import sqrt, pi  
print(sqrt(16)) 
print(pi)  

#Importing a Module with an Alias
import random as r  
print(r.randint(1, 10)) 

#User-Defined Module
import module  
print(module.greet("Code Queen")) 
print(module.pi_value) 

#Using External Modules
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
