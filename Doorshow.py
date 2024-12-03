import random

print("Welcome to the Monty's Hall Game")
doors=[1,2,3]
host=random.choice(doors)
participant=int(input("Choose a door(1,2,3):"))
if participant==host:
    print("The host opens the door",participant,"revealing a car.CONGRATULATIONS!,You won")
else:
    print("The host opens the door",participant,"revealing the goat")
    reply=input("Do you want to switch your choice? (yes/no) ")
    if reply==' yes':
        revised=int(input("Select another option "))
        if revised==host:
            print("Congratulations!,You won the car")
        else:
            print("The host opens the door",participant,"revealing the goat")

    if reply=='no':
        print("You have got a goat,so you lose")
