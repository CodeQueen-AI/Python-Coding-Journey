# Binary Language
print(bin(10)) 

#Assembly Language
import ctypes
print(ctypes.c_int(10).value)

# #C/C++ (Low-Level Languages)
import ctypes
libc = ctypes.CDLL("msvcrt.dll")  
libc.printf(b"Hello from C!\n")

# #SQL (Database Language)
import sqlite3
conn = sqlite3.connect(":memory:")
print("Database Connected!")
