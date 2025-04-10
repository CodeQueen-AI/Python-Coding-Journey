#Unicode Characters
print("\u0939\u0947\u0932\u094b") 
print("\u0633\u0644\u0627\u0645")  

#ASCII
print(ord('A'))
print(chr(97))  

#UTF-8
text = "Hello, 你好, مرحبا"
encoded_text = text.encode("utf-8")  
print(encoded_text)  
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)  