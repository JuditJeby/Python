check_number=int(input("Enter the number"))
for number in range(2,check_number+1):
    prime = True
    for i in range(2,(number//2)+1):
      if number%i==0:
        prime=False
        break
    if prime:
     print(number)