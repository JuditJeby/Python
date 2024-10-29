"""Author Judit Jeby
   Created on 29 10 14"""

str1=(input("Enter the string :"))
vowels="aeiouAEIOU"
vowels_count=0
for char in str1:
    if char in vowels:
        vowels_count+=1
print(f"The number of vowels in {str1} is {vowels_count}")