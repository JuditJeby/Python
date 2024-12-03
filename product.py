"""
Author-Judit Jeby
Created on 03-12-24
Python program to find the product of a number using function


"""
def product(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+product(n1,n2-1)
multiplication=product(5,4)
print(multiplication)