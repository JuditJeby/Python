a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
sum=a+b
division=a/b
print("sum :",sum, end=",")
print("division :",division)

print("Is a greater then b ?", end="  ")
print(a>b)

print("Are a and b equal?", end=" " )
print(a==b)
print("Logical AND:", end="")
print( (a>b) and (b<a))

print("Logical OR:",end="")
print((a>=b) or (b<=a))