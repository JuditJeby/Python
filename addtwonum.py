"""
Author-Judit Jeby
Created on 03-12-24
Python program to find the sum of two numbers
using function

"""

def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
         return add_numbers(n1+1,n2-1)
sum=add_numbers(5,3)
print(sum)
