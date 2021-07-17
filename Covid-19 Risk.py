#!/usr/bin/env python
# coding: utf-8

# In[3]:


age = str(input("Are you a cigarette addict older than 75 years old? yes or no: ")).title().strip() == "Yes"
chronic = str(input("Do you have a severe chronic disease? yes or no: ")).title().strip() == "Yes"
immune = str(input("Is your immune system too weak? yes or no: ")).title().strip() == "Yes"
if (age or chronic or immune):
    print("You are in risky group")
else:
    print("You are not in risky group")


# In[ ]:





# In[ ]:




