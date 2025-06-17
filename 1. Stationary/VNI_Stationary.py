#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
from statsmodels.tsa.stattools import adfuller
# Read CSV file
file_path = "VNI_data.csv"  
df = pd.read_csv(file_path)  
df.rename(columns={"Lần cuối": "Giá"}, inplace=True)
df_new = df[['Ngày', 'Giá']].copy()  
df_new['Giá'] = df_new['Giá'].astype(str).str.replace(',', '', regex=True).astype(float)
df_new["Ngày"] = pd.to_datetime(df_new["Ngày"], format="%d/%m/%Y") 
df_new = df_new[df_new["Ngày"] >= "2020-01-01"]
df_new = df_new.sort_values(by="Ngày", ascending=True).reset_index(drop=True)

# Stationary test 
df_new.dropna( inplace=True)
result = adfuller(df_new["Giá"])
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:")
for key, value in result[4].items():
    print(f"  {key}: {value:.6f}") 
print('P_value > 5%, Not stationary and take percentage change.')
print('')

# Take Percentage change
df_new["PCT_VNI"] = df_new["Giá"].pct_change() * 100
df_new.dropna( inplace=True)
df_new
df6 = df_new[['PCT_VNI']]
# Stationary test again
result = adfuller(df_new["PCT_VNI"])
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:")
for key, value in result[4].items():
    print(f"  {key}: {value:.6f}")
print('P_value < 5%, Stationary.')

