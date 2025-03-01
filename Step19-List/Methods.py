#Methods of List
#Append()
fruits = ["apple", "banana"]
fruits.append("grapes")  
print(fruits)  

#Insert()
fruits = ["🍎 apple", "🍌 banana"]
fruits.insert(1, "🍉 watermelon")  
print(fruits)  

#Remove()
fruits = ["🍎 apple", "🍌 banana", "🍒 cherry"]
fruits.remove("🍌 banana")  
print(fruits)  

#Pop()
fruits = ["🍎 apple", "🍌 banana", "🍒 cherry"]
fruits.pop()  
print(fruits)  

fruits.pop(0)    
print(fruits)  

#Sort()
numbers = [3, 1, 4, 2]
numbers.sort()  
print(numbers)  

#Reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()  
print(numbers)  

#Index()
fruits = ["🍎 apple", "🍌 banana", "🍒 cherry"]
print(fruits.index("🍌 banana"))  

#Count()
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))  

#Extend()
fruits = ["🍎 apple", "🍌 banana"]
more_fruits = ["🍉 watermelon", "🍇 grapes"]
fruits.extend(more_fruits)  
print(fruits)  

#Clear()
fruits = ["🍎 apple", "🍌 banana"]
fruits.clear()  
print(fruits)  

#Copy()
fruits = ["🍎 apple", "🍌 banana", "🍇 grapes"]
new_fruits = fruits.copy()

# New list ko modify karna
new_fruits.append("🍉 watermelon")

print("Original List:", fruits)  
print("Copied List:", new_fruits)  

#sort(reverse=True)
numbers = [5, 2, 8, 1, 4]
numbers.sort(reverse=True) 
print(numbers)  

#del()
fruits = ["🍎 apple", "🍌 banana", "🍒 cherry"]
del fruits[1] 
print(fruits)  

numbers = [1, 2, 3, 4]
del numbers 
