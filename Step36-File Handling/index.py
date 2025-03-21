# r - Read Mode 
with open("index.py", "r") as file:
    data = file.read()
    print("Read Mode Data:\n", data)

# w - Write Mode
with open("write_mode.html", "w") as file:
    file.write("Hello World")

# a - Append Mode 
with open("write_mode.html", "a") as file:
    file.write("\nNew Line Added!")

# x - Exclusive Creation Mode 
# It will create a new file if it does not exist
with open("new_file.txt", "x") as file:
    file.write("This is a new file created using 'x' mode.")
print("File successfully created!")

#When the file already exists
try:
    with open("new_file.txt", "x") as file:
        file.write("Trying to create a file that already exists.")
except FileExistsError:
    print("Error: File already exists!")

# wb - Write Binary Mode 
with open("example.bin", "wb") as file:
    file.write(b'\x00\x01\x02\x03')

# r+ - Read & Write Mode 
with open("write_mode.html", "r+") as file:
    data = file.read()
    file.write("\nAppending in r+ mode")

# rb - Read Binary Mode
with open("image.jpg", "rb") as file:
    data = file.read()
    print("Binary Data of Image:", data[:20]) 
    
# Copying Binary Data (rb + wb combination)
with open("image.jpg", "rb") as source:
    data = source.read()

with open("copy_image.jpg", "wb") as destination:
    destination.write(data)
