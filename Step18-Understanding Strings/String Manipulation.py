#String Slicing  
text = "Programming"
print(text[0:5])   
print(text[-5:]) 

# String Concatenation 
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  

#String Repetition (*)
text = "Python"
print(text * 3)  

#String Splitting & 
text = "Hello,World,Python!"
words = text.split(",") 
print(words)

#String Joining
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)
 
#string Formatting
name = "Code Queen"
age = 17
print(f"My name is {name} and I am {age} years old")  
