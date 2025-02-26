#Indentation
if True:
    print("Indented correctly")  # ✅ 
    
# if True:
# print("This will give an error!")   ❌ 

#Case Sensitive
name = "Alice"
print(name) 
Name = "Bob"
print(Name) 

#Comments
print("Hello, Python!")  # Yeh print hoga, magar comment ignore hoga

"""
Yeh aik multi-line comment hai.
Jo multiple lines mei likha ja sakta hai.
"""
print("Python is fun!")

#End of Statement
print("Hello, Python!")  # ✅ 
#print("Hello"); print("Python") ❌ 

#Printing Output print() function
print("Hello, World!")

#User Input
name = input("What's Your Name: ")
print("Hello,", name)

#Variable Declaration
age = 25      # Integer
print(age)
name = "Ali"  # String
print(name)
price = 99.99 # Float
print(price)

#Line Continuation
total = (10 + 20 +
         30 + 40)  # Parentheses ka istemal
print(total)
message = "Yeh aik lambi string hai " \
          "jo multiple lines pe likhi gayi hai"
print(message)