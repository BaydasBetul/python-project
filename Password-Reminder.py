#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = input("Please enter your name:").title().strip()
user_name = "Joseph"
user_password = "W@12" 
if name == user_name:
    print("Hello, {}! The password is :{}".format((user_name),(user_password)))
else:
  print("Hello, {}! See you later.".format(user_name))

