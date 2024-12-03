"""
Author-Judit Jeby
Created on 03-12-24
Python program to find the factorial of a number using function


"""

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n - 1)

f=factorial(5)
print(f)

