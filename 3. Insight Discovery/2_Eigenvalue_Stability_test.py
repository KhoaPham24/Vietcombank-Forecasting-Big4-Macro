#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR

# Eigenvalue
eigenvalues = result.roots  
modulus = np.abs(eigenvalues)  

# Result
print("Eigenvalues of VAR:")
print(eigenvalues)

print("\nModulus of Eigenvalues:")
print(modulus)

print('Not Stable')

