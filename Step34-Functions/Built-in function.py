#map() 
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  

#filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  


#reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]

# Find the sum of all numbers
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result) 

#Find Maximum in List)
from functools import reduce
numbers = [10, 5, 30, 20]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)

#zip()
names = ["CodeQueen", "Anusha", "Ifra"]
scores = [95, 88, 76]
combined = list(zip(names, scores))
print(combined)  

#(Unzipping Using zip(*iterable))
combined = [('CodeQueen', 95), ('Anu', 88), ('Ifra', 76)]
names, scores = zip(*combined)
print(names)
print(scores)  

#sorted()
#Ascending Order
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  

#Descending Order
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)  

#Sorting with Custom Key -
words = ["banana", "apple", "cherry", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words) 

#enumerate()
names = ["CodeQueen", "Anu", "Ifra"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

#(Custom Start Index)
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
