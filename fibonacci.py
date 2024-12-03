"""Author:Judit Jeby
Date:3-12-2024
Python porgram to generate fibonacci numbers"""

def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for i  in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibonacci(10))

