#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import matplotlib.pyplot as plt

eigenvalues = result.roots

# Draw unit root
fig, ax = plt.subplots(figsize=(6,6))
unit_circle = plt.Circle((0, 0), 1, color='b', fill=False, linestyle='dashed')
ax.add_patch(unit_circle)
plt.scatter(eigenvalues.real, eigenvalues.imag, color='red', label='Eigenvalues')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.title("Eigenvalues and Unit Circle")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.legend()
plt.grid()

# Show
plt.show()

