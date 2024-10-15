"""
Python program to find the sum of digits of the given number
"""



number=int(input("Enter the number:"))
number1=number
sum=0
while number>0:
    r=number%10
    number=number//10
    sum=sum+r
print("The sum of  digits of the number",number1,"is",sum)
