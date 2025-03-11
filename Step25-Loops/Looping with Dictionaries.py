student = {"name": "CodeQueen", "age": 17, "grade": "A"}

# Looping through keys
for key in student:
    print(key)

# Looping through values
for value in student.values():
    print(value)

# Looping through both keys and values
for key, value in student.items():
    print(key, ":", value)
