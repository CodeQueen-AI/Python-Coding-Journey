#Function Scope
def example():
    x = 10 
    print(x)  

example()  
print(x) 

#Block Scope
if True:
    y = 20  
print(y)
