A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# Subset
print(A <= B)  
print(A.issubset(B))  

# Proper Subset
print(A < B)  

# Superset
print(B >= A)  
print(B.issuperset(A))  

# Proper Superset
print(B > A)  

# Disjoint Sets
print(A.isdisjoint(C))  