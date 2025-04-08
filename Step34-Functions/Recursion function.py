#Factorial Calculation
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1) 
    
print(factorial(5)) 

#Fibonacci Series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

print(fibonacci(6)) 


#Sum of N Natural Numbers
def sum_n(n):
    if n == 0:  
        return 0
    else:
        return n + sum_n(n - 1) 

print(sum_n(5)) 


#Reverse a String Using Recursion
def reverse_string(s):
    if len(s) == 0: 
        return s
    else:
        return s[-1] + reverse_string(s[:-1])  
    
print(reverse_string("code"))  


#Optimized Fibonacci Using Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(fibonacci_memo(50))  