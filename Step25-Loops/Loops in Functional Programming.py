from functools import reduce

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, nums))  
evens = list(filter(lambda x: x % 2 == 0, nums)) 
sum_all = reduce(lambda x, y: x + y, nums) 
print(squares)
print(evens)
print(sum_all)