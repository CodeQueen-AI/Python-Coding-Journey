#upper()
text = "hello code queen"
print(text.upper())  

#strip()
text = "  Hello  "
print(text.strip())  

#replace(old, new)
text = "I love Js"
print(text.replace("Js", "Python"))  

#split(separator)
text = "apple,banana,grape"
fruits = text.split(",")  
print(fruits)  

#join(iterable)
words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)  

#find(substring)
text = "Hello Code Queen"
print(text.find("Code"))  

#count(substring)
text = "banana"
print(text.count("a"))  

# startswith(substring) & endswith(substring)
text = "Python is fun"
print(text.startswith("Python")) 
print(text.endswith("fun"))  

#capitalize
text = "hello world"
print(text.capitalize())  

#title()
text = "hello code queen"
print(text.title())  

#swapcase()
text = "Hello Code Queen"
print(text.swapcase())  

#isalpha()
text = "Hello"
print(text.isalpha())

text = "Hello123"
print(text.isalpha())  

#isdigit()
text = "12345"
print(text.isdigit()) 

text = "123abc"
print(text.isdigit())  

#isalnum()
text = "Python123"
print(text.isalnum())  

text = "Python 123"
print(text.isalnum())  
