# Frozen Set Banana
fruits = frozenset(["Apple", "Banana", "Cherry"])
print(fruits)  

# Membership Check
print("Apple" in fruits)  
# Output: True

# Iterating Over Frozen Set
for fruit in fruits:
    print(fruit)

# Set Operations (Union, Intersection)
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])

union_set = set1 | set2  
print(union_set)  

intersection_set = set1 & set2  
print(intersection_set)  
