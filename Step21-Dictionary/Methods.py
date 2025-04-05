#Keys()
student = {
    "name": "CodeQueen",
    "age": 17,
    "grade": "A",
    "city": "Karachi"
}
print(student.keys())

#Values()
student = {
    "name": "Anusha",
    "age": 19,
    "grade": "B",
    "city": "Karachi"
}
print(student.values())  

#Items()
student = {
    "name": "Jiya",
    "age": 21,
    "grade": "C",
    "city": "Karachi"
}
print(student.items())  

#Get()
student = {
    "name": "Ifra",
    "age": 16,
    "grade": "D",
    "city": "Karachi"
}
print(student.get("grade"))  

#Update()
student = {
    "name": "Fatima",
    "age": 23,
    "grade": "E",
    "city": "Karachi"
}
student.update({"height": "5'6", "city": "Lahore"})
print(student)  

#Pop()
student = {
    "name": "Quratulain",
    "age": 25,
    "grade": "A",
    "city": "Karachi"
}
age = student.pop("age")
print(age) 
print(student)  

#PopItems()
student = {
    "name": "CodeQueen",
    "age": 17,
    "grade": "A",
    "city": "Karachi"
}
student.popitem()
print(student)  

#Clear()
student = {
    "name": "CodeQueen",
    "age": 17,
    "grade": "A",
    "city": "Karachi"
}
student.clear()
print(student)  

#copy()
student = {
    "name": "CodeQueen",
    "age": 17
}
new_student = student.copy()
print(new_student)  

#Del()
student = {
    "name": "CodeQueen",
    "age": 17
}
del student["age"]  
print(student)  

del student  

#setdefault()
student = {
    "name": "CodeQueen",
    "age": 17
}
result = student.setdefault("name", "Unknown")  
print(result) 
print(student)  

#Key does not exist
student = {
    "name": "CodeQueen",
    "age": 17
}
result = student.setdefault("grade", "A")  
print(result)  

print(student)  

#formkeys(Iterable,value)
keys = ["name", "age", "grade"]
default_value = "Not available"
student = dict.fromkeys(keys, default_value)
print(student)  


