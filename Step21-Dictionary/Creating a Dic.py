# Empty Dictionary
my_dict = {}
print(my_dict)  

# Dictionary with Values
person = {"name": "CodeQueen", "age": 17, "city": "Karachi"}
print(person)

# Using dict() Constructor
student = dict(name="Anusha", age=20, grade="A")
print(student)

# Creating Dictionary with zip()
keys = ["name", "age", "city"]
values = ["Ifra", 16, "Lahore"]
person = dict(zip(keys, values))
print(person)

# Nested Dictionary
students = {
    "student1": {"name": "Quratulain", "age": 23},
    "student2": {"name": "Jiya", "age": 21}
}
print(students)
