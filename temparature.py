"""Author -Judit Jeby
   Created on 22/10/24
   Pyhton program about converting celsious to fahrenheit
"""


temperature=int(input("Enter  temperatue :"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")

if(unit=="c"):
    fahrenheit = ((9/5) * temperature) + 32
    print(temperature,"Celsious is",fahrenheit,"Fahrenheit")
else:
    celsious = 5/9 *(temperature-32)
    print(temperature,"Fahrenheit is",  celsious,"Celsious")
