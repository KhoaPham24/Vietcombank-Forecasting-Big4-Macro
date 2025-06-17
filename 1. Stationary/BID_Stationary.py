#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
from statsmodels.tsa.stattools import adfuller
# Read CSV file
file_path = "BID_data.csv"  
df = pd.read_csv(file_path, delimiter=",")  
df.rename(columns={"Lần cuối": "BID"}, inplace=True)
df_new = df[['Ngày', 'BID']].copy()  
df_new['BID'] = df_new['BID'].str.replace(',', '', regex=True).astype(float)
df_new["Ngày"] = pd.to_datetime(df_new["Ngày"], format="%d/%m/%Y") 
df_new = df_new[df_new["Ngày"] >= "2020-01-01"]
df_new = df_new.sort_values(by="Ngày", ascending=True).reset_index(drop=True)
df2 = df_new[['BID']]
# Stationary test 
df_new.dropna( inplace=True)
result = adfuller(df_new["BID"])
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:")
for key, value in result[4].items():
    print(f"  {key}: {value:.6f}") 
print('P_value > 5%, Not stationary and take percentage change.')
print('')

