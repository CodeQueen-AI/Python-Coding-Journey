#Constructor Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("CodeQueen", 17)
print(person1.name) 
print(person1.age)  

#__str__ (String Representation of Object)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person1 = Person("CodeQueen", 17)
print(person1)

#(__len__ & __getitem__)
class Numbers:
    def __init__(self, nums):
        self.nums = nums

    def __len__(self):
        return len(self.nums)

    def __getitem__(self, index):
        return self.nums[index]

numbers = Numbers([10, 20, 30])
print(len(numbers))
print(numbers[1])  
