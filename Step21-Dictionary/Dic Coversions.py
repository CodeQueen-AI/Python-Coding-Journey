import json

# Dictionary to List
my_dict = {"a": 1, "b": 2, "c": 3}
keys_list = list(my_dict.keys())    
values_list = list(my_dict.values()) 
items_list = list(my_dict.items())   
print(keys_list, values_list, items_list)

# Dictionary to Tuple
my_dict = {"x": 10, "y": 20}
items_tuple = tuple(my_dict.items()) 
print(items_tuple)

# Dictionary to JSON
my_dict = {"name": "Code Queen", "age": 22, "city": "Lahore"}
json_data = json.dumps(my_dict) 
print(json_data)
