#Creating a MemoryView
data = bytearray("Hello", "utf-8")  
data1 = memoryview(data)  
print(data1[0]) 
print(data1[:])  

#Modifying Data Without Copying 
data = bytearray("Hello", "utf-8")
data1 = memoryview(data)
data1[0] = 74  
print(data) 

#Slicing in MemoryView
data = bytearray("Python", "utf-8")
data1 = memoryview(data)
print(data1[2:])  
print(data1[2:].tobytes())  