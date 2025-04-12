#Dictionary Unpacking in a Function
def show_details(name, age):
    print(f"Name: {name}, Age: {age}")
person = {"name": "Code Queen", "age": 22}
show_details(**person)  

#Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2} 
print(merged_dict)

# Capturing Extra Arguments in a Function
def show_info(**kwargs):
    print(kwargs)
show_info(name="Code Queen", age=22, city="Lahore")
