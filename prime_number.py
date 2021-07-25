#!/usr/bin/env python
# coding: utf-8

# In[4]:


while True:
    sayi = (input("Sayıyı Girin : "))
    if sayi.isdigit() == True:
         sayi =int(sayi)
    break
    
if sayi > 1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print(sayi," Asal Sayı Değildir.")
            break
    else:
        print(sayi," Asal Sayıdır.")

else:
    print(sayi," Asal Sayı Değildir.")


# In[ ]:





# In[ ]:




