#No Return
def greet():
    print("Hello, Code Queen!")

result = greet() 
print(result)   

#Returning a Single Value
def square(n):
    return n * n

print(square(5))  

#Returning Multiple Values
def get_coordinates():
    return 10, 20 

x, y = get_coordinates()
print(x, y) 

#Returning a List
def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_numbers())

#Returning a Dictionary
def get_student():
    return {"name": "CodeQueen", "age": 17}

print(get_student())

#Returning a Function (Higher-Order Function)
def outer_function():
    def inner_function():
        return "Hello from Inner Function!"
    return inner_function

func = outer_function()
print(func()) 

#Returning a Lambda Function
def multiply_by(n):
    return lambda x: x * n

double = multiply_by(2)
print(double(5))  
