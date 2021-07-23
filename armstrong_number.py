#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    number=input("Please enter a positive integer number: ")
    if number.isdigit():
        break      
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    continue
  
num = int(number)
top = 0
sayi = num
while sayi > 0:
    digit = sayi % 10    
    top += digit ** len(str(num))   
    sayi //= 10
if num == top:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

