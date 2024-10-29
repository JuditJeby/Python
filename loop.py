check_number=int(input("Enter the number"))
prime= True
for i in range(2,(check_number//2)+1):
     if check_number % i ==0:
         Prime=False
         break
if prime:
     print(f"The given number {check_number} is prime")
else:
    print(f"The given number {check_number} is prime")
