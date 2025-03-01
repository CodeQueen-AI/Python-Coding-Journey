#Creating a Nested List  
matrix = [
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]
]
print("Original Matrix:", matrix)

#Accessing Elements in a Nested List  
print(matrix[0])      
print(matrix[1][2])  

#Iterating Over Nested Lists 
for row in matrix:
    for num in row:
        print(num, end=" ")  
print() 

#Modifying a Nested List 
matrix[1][1] = 50  
print("Updated Matrix:", matrix)

#Adding and Removing Lists  
matrix.append([10, 11, 12])  
print("After Adding a Row:", matrix)

del matrix[0]  
print("After Removing a Row:", matrix)

#List Comprehension with Nested Lists  
squared_matrix = [[num**2 for num in row] for row in matrix]
print("Squared Matrix:", squared_matrix)
