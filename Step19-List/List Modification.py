#Updating Elements 
fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Mango"  
print(fruits)

#Adding Elements
#append()
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Orange")   
print(fruits)
#insert()             
fruits = ["Apple", "Banana", "Cherry"]
fruits.insert(1, "Grapes")  
print(fruits)
#extend() 
fruits = ["Apple", "Banana", "Cherry"]
more_fruits = ["Pineapple", "Watermelon"]
fruits.extend(more_fruits) 
print(fruits)

#Removing Elements
fruits = ["Apple", "Banana", "Cherry"]

#append()
fruits.append("Mango")  
print("After Append:", fruits)  

fruits.remove("Mango")  
print("After Remove:", fruits) 

#insert() 
fruits.insert(1, "Grapes")  
print("After Insert:", fruits) 

fruits.pop(1)  
print("After Pop:", fruits) 

#extend()
more_fruits = ["Cherry", "Mango"]
fruits.extend(more_fruits)  
print("After Extend:", fruits)  

fruits.clear()  
print("After Clear:", fruits)  
