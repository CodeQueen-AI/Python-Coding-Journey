#Parameters
def add(a, b):  
    return a + b

result = add(5, 3) 
print(result)

#Positional Parameters
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("CodeQueen", 17)  

# Default Parameters
def greet(name="Code Queen"):
    print(f"Hello, {name}!")

greet() 
greet("Anusha")  

#Keyword Parameters
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info(age=17, name="CodeQueen")  

#Arbitrary Positional Parameters
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

add_numbers(2, 4, 6, 8)

#Arbitrary Keyword Parameters
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="CodeQueen", age=17, city="Karachi")


