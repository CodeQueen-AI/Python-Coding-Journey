#Function Scope
def example():
    x = 10 
    print(x)  

example()  
print(x)  #Error: x is not defined

#Block Scope
if True:
    y = 20  
print(y)
