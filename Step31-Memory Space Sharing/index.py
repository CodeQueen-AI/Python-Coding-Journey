#Integer Memory Sharing
a = 100
b = 100
print(a is b)  # Output: True 

#If a number is greater than 256, separate memory is allocated
x = 300
y = 300
print(x is y)  # Output: False 

#String Memory Sharing
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # Output: True 

#If a string is created dynamically, separate memory is allocated
s3 = "world"
s4 = "".join(["wo", "rld"]) 
print(s3 is s4)  

#List Memory Sharing
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  

#But if a list is assigned to another variable, the memory is shared
list3 = list1  
print(list1 is list3)  # Output: True 
