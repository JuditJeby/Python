temp=int(input("Enter  temperatue :"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")

if(unit=="c"):
    f = ((9/5) * temp) + 32
    print(temp,"Celsious is",f,"Fahrenheit")
else:
    c = 5/9 *(temp-32)
    print(temp,"Fahrenheit is",c,"Celsious")
