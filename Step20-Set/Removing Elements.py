fruits = {"Apple", "Banana", "Cherry"}

# remove() method 
fruits.remove("Banana")  
print(fruits)

# discard() method 
fruits.discard("Cherry") 
print(fruits) 

fruits.discard("Mango")  
print(fruits)  

# pop() method
removed_item = fruits.pop()  
print(removed_item)  
print(fruits)  

# clear() method 
fruits.clear()
print(fruits)  
