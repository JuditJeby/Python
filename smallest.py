"""
Author -Judit Jeby
Created on 15/10/2024
Program to find the smallest number among three number
"""

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1<num2 and num1<num3:
    print("The smallest number is :",num1)
elif num2<num1 and num2<num3:
    print("The smallest number is :", num2)
else:
    print("The smallest number is :", num3)
