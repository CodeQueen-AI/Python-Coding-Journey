# Simple Set Comprehension (Square of Numbers)
numbers = {x**2 for x in range(5)}
print(numbers)  

# Filtering with Condition (Even Numbers Only)
even_numbers = {x for x in range(10) if x % 2 == 0}
print(even_numbers)  

# Removing Duplicates from a List
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = {x for x in duplicates}
print(unique_set)  

# Converting Strings to Uppercase
words = {"apple", "banana", "cherry"}
uppercase_set = {word.upper() for word in words}
print(uppercase_set)  

