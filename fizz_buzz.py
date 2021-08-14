#!/usr/bin/env python
# coding: utf-8

# In[1]:



def fizz_buzz(num):
    
    for i in range(1, num+1):
       if not i % 15:
           print('FizzBuzz')
       elif not i % 5:
           print('Buzz')
       elif not i % 3:
           print('Fizz')
       else:
           print(i)
    return i
print(fizz_buzz(100)) 


# In[ ]:




