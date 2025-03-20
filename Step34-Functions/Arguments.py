#Arguments
def greet(name):
    print("Hello, " + name + "!")

greet("Code Queen")

#Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("CodeQueen", 17)  

#Default Arguments
def greet(name="Code Queen"):
    print(f"Hello, {name}!")

greet()  
greet("CodeQueen") 

#Keyword Arguments
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info(age=17, name="CodeQueen")  

#Arbitrary Arguments
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

add_numbers(2, 4, 6, 8) 

#Arbitrary Keyword Arguments
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="CodeQueen", age=17, city="Karachi")
