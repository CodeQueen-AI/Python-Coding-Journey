def multiply(x):
    def inner(y):
        return x * y
    return inner
double = multiply(2) 
print(double(5))
print(double(10))  

#Using lambda for Currying
multiply = lambda x: lambda y: x * y
double = multiply(2) 
print(double(5))