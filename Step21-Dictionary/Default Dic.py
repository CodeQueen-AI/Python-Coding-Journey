from collections import defaultdict

# defaultdict(int) 
int_dict = defaultdict(int)
int_dict['a'] += 1  
print(int_dict) 

# defaultdict(list) 
list_dict = defaultdict(list)
list_dict['b'].append(10)  
print(list_dict)  

# defaultdict(set) 
set_dict = defaultdict(set)
set_dict['c'].add(20) 
print(set_dict)  

# defaultdict(str) 
str_dict = defaultdict(str)
str_dict['d'] += "Hello"  
print(str_dict)

# Default dictionary example
normal_dict = defaultdict(lambda: "Not Found") 
print(normal_dict['e']) 
