number=int(input("Enter the number"))
fact=1
while number>0:
    fact=fact*number
    number-=1
print("The factorial is",fact)