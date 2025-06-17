#!/usr/bin/env python
# coding: utf-8

# In[34]:


from statsmodels.tsa.api import VAR

model = VAR(df_mix.drop(columns=['Ngày'])) 
lag_selection = model.select_order(maxlags=10)  
print(lag_selection.summary())

