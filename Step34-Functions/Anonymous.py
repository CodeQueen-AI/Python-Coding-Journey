# Normal function
def square(x):
    return x * x
print(square(5))  

# Lambda function
square_lambda = lambda x: x * x
print(square_lambda(5)) 

#Multiple Parameters in Lambda
add = lambda x, y: x + y
print(add(3, 7))  

#Lambda with map & filter
numbers = [1, 2, 3, 4, 5]

# Squaring each number using map
squared = list(map(lambda x: x * x, numbers))
print(squared)  

# Filtering even numbers using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  
