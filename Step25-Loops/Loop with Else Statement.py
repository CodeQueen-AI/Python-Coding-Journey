for num in range(1, 6):  
    print(num)  
else:  
    print("Loop completed successfully!")  


#If a loop stops with a break statement, the else block does not execute
for num in range(1, 6):  
    if num == 3:  
        break  
    print(num)  
else:  
    print("Loop completed!") 