#Named Functions
def greet(name):
    print(f"Hello, {name}!")

greet("CodeQueen")  

#Anonymous Functions
square = lambda x: x * x  
print(square(5))  

#Arrow Functions
square = lambda x: x * x  
print(square(5))  

#Immediately Invoked Function Expressions (IIFE)
(lambda x: print(f"Hello, {x}!"))("CodeQueen")

#Higher-Order Functions
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x * x, 5)
print(result)  