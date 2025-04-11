#String Pool
s1 = "hello"
s2 = "hello"
print(s1 is s2)  

#String Interning
import sys
s1 = sys.intern("world")
s2 = sys.intern("world")
print(s1 is s2)  

s1 = "python"
s2 = "".join(["py", "thon"])  
print(s1 is s2) 
