#Zero Division
#Error Without Exception Handling
num1 = 10
num2 = 0
print(num1 / num2)  

#Correct Way of Exception Handling

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This message will always be printed")


#Value Error
#Error Without Exception Handling
age = int(input("Enter your age: "))  #If the user enters "abc," an error will occur
print(f"Your age is {age}")

#Correct Way of Exception Handling
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Error: Please enter a valid number!")   


#TypeError
#Error Without Exception Handling
num = 5 + "hello"  #Adding an integer and a string is invalid

#Correct Way of Exception Handling
try:
    num = 5 + "hello"
except TypeError:
    print("Error: You cannot add an integer and a string!")   
    

#IndexError
#Error Without Exception Handling
my_list = [10, 20, 30]
print(my_list[5]) #Index 5 does not exist

#Correct Way of Exception Handling
try:
    my_list = [10, 20, 30]
    print(my_list[5])
except IndexError:
    print("Error: This index does not exist in the list!")


#KeyError
#Error Without Exception Handling
my_dict = {"name": "Alice", "age": 25}
print(my_dict["city"]) #The 'city' key does not exist

#Correct Way of Exception Handling
try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["city"])
except KeyError:
    print("Error: This key does not exist in the dictionary!")
  

#Handling Multiple Exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Enter numbers only, not alphabets!")
except Exception as e:
    print(f"Some other error occurred: {e}")
finally:
    print("Program has completed")
