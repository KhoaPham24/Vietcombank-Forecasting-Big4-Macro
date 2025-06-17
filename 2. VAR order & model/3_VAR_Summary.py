#!/usr/bin/env python
# coding: utf-8

# In[33]:


df_combined = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
df_mix = df_combined.dropna()
df_mix

