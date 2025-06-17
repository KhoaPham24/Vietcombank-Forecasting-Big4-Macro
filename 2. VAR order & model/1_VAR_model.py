#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Using lag(1) from the result of choosing lag above
var_model = model.fit(1)  
print(var_model.summary())

