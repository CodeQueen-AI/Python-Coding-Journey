#Bytes
data = b"Hello"  
print(data) 
# data[0] = 80  # TypeError: 'bytes' object does not support item assignment

#BytesArray
data = bytearray(b"Hello")  
data[0] = 80 
print(data)
