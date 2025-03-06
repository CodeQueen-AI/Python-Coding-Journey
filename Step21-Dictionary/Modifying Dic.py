# Updating a Value
person = {"name": "CodeQueen", "age": 17}
person["age"] = 26  
print(person)  

# Adding a New Key-Value Pair
person["city"] = "Karachi"
print(person)  

# Removing a Key-Value Pair using pop()
removed_value = person.pop("age")
print(person) 
print(removed_value)  

# Removing the Last Inserted Pair using popitem()
person["country"] = "Pakistan"
person.popitem()
print(person)  

# Clearing All Items using clear()
person.clear()
print(person)  

# Merging Dictionaries using update()
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1) 
