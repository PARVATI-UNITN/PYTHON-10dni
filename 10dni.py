#!/usr/bin/env python
# coding: utf-8

# Convert seconds into hours, minutes, and seconds.

# In[10]:


#i:
second=int(input("ENTER TIME IN SECONDS "))
hours=second//3600
minutes=(second%3600)//60
seconds=(second%3600)%60
print(second ,"seconds is ",hours,"hr:",minutes,"min:",seconds,"secs")


# In[9]:


#ii:
second=int(input("ENTER TIME IN SECONDS "))
minute=second//60
seconds=second%60
hours=minute//60
minutes=minute%60
print(f"{second} seconds is {hours}hr:{minutes}min:{seconds}secs")

