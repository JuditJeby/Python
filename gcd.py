"""
Author-Judit Jeby
Created on 03-12-24
Python program to find the greatest common dinominator using function


"""
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
common=gcd(100,3)
print(common)