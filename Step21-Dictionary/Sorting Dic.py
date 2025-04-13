#Sorting a dictionary by keys
my_dict = {"b": 2, "a": 1, "c": 3}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)  

#Sorting a dictionary by values
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)  
