nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for sub_tuple in nested_tuple:  
    for item in sub_tuple:     
        print(item, end=" ")
    print()  
