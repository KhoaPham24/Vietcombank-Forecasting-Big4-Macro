#!/usr/bin/env python
# coding: utf-8

# In[35]:


import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

# Create IRF with 4 periods
irf = result.irf(4)
fig = plt.figure(figsize=(200, 10)) 
irf.plot(orth=True)  
plt.suptitle("Overall Impulse Response (IRF)", fontsize=16, fontweight="bold")
plt.show()

