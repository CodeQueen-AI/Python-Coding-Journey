import json

# Python Dictionary to JSON
my_dict = {"name": "Code Queen", "age": 22}
json_data = json.dumps(my_dict)
print(json_data) 

# JSON to Python Dictionary
json_string = '{"name": "Code Queen", "age": 22}'
dict_data = json.loads(json_string)
print(dict_data["name"]) 
