# Basic List Comprehension 
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) 

# Conditional List Comprehension 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  

# String Manipulation with List Comprehension 
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  

# Nested Loop List Comprehension 
matrix = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(matrix)  
