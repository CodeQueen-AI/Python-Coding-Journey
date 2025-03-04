A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(A | B)  
print(A.union(B))  

# Intersection 
print(A & B)  
print(A.intersection(B))  

# Difference 
print(A - B)  
print(A.difference(B))  

# Symmetric Difference 
print(A ^ B)  
print(A.symmetric_difference(B))  

# Subset 
print(A <= B)  
print(A.issubset(B))  

# Superset 
print(A >= B)  
print(A.issuperset(B))  

# 7️⃣ Disjoint Sets 
print(A.isdisjoint(B))  