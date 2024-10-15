"""
Author -Judit Jeby
Created on 15/10/2024
Program to know the ticket fee according to the person"s age
"""




age=int(input("Enter the age :"))
if age<10:
    print("The ticket fee for the person is 7")
elif 10<= age <=60:
    print("The ticket fee for the person is 10")
else:
    print("The ticket fee for the person is 5")