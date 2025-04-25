# Add()
fruits = {"Apple", "Banana"}
fruits.add("Grape")
print(fruits)

# Remove()
fruits = {"Apple", "Banana"}
fruits.remove("Banana")
print(fruits)

# Discard
fruits = {"Apple", "Banana"}
fruits.discard("Banana") 
print(fruits)

# Pop()
fruits = {"Apple", "Banana", "Orange"}
fruits.pop()
print(fruits)

# Clear()
fruits = {"Apple", "Banana"}
fruits.clear()
print(fruits)

# Union()
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
new_set = set1.union(set2)
print(new_set)

# Intersection()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
common = set1.intersection(set2)
print(common)

# Difference()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
diff = set1.difference(set2)
print(diff)

# Symmetric Difference()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Orange", "Pineapple"}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)

# Copy()
fruits = {"Apple", "Banana"}
new_fruits = fruits.copy()
print(new_fruits)

# isdisjoint()
set1 = {"Apple", "Banana"}
set2 = {"Orange", "Pineapple"}
print(set1.isdisjoint(set2))

# issubset()
set1 = {"Apple", "Banana"}
set2 = {"Apple", "Banana", "Orange"}
print(set1.issubset(set2))

# issuperset()
set1 = {"Apple", "Banana", "Orange"}
set2 = {"Apple", "Banana"}
print(set1.issuperset(set2))
