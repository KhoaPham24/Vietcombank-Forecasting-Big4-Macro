#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Detail IRF
for var in df_var.columns:
    irf.plot(impulse=var)
    plt.title(f"Detail Impulse Response Function (IRF) - {var}")
    plt.show()

