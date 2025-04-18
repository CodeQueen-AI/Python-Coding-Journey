#Dictionary
my_dict = {"name": "CodeQueen", "age": 17, "city": "Karachi"}

#Loop Through Keys
for key in my_dict:
    print(key)

#Loop Through Values
for value in my_dict.values():
    print(value)

# Loop Through Key-Value Pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Loop Through Dictionary Using enumerate()
for index, (key, value) in enumerate(my_dict.items()):
    print(f"{index}: {key} → {value}")

#Loop Through a Nested Dictionary
students = {
    "student1": {"name": "Anusha", "age": 19},
    "student2": {"name": "ifra", "age": 17}
}

for student, details in students.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key} → {value}")
