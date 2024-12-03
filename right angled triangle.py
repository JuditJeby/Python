



def triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    larger = (max(sides))
    sides.sort()
    if larger*larger==(sides[0]*sides[0])+(sides[1]*sides[1]):
        return True
    return False
side1=int(input("Enter the first side"))
side2=int(input("Enter the second side"))
side3=int(input("Enter the third side"))
triangle(side1,side2,side3)
if triangle(side1,side2,side3 ):
    print("Right angled triangle")
else:
    print("Not right angled triangle")
triangle(side1,side2,side3)



