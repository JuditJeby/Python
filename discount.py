amount=int(input("Enter the amount:"))
if amount>500:
    discount = amount * 20 / 100
    final_amount = amount - discount
    print("The final amount is:", final_amount)
elif  500>=amount>=200:
    discount = amount * 10 / 100
    final_amount = amount - discount
    print("The final amount is:", final_amount)
else:
    print("No discount")
