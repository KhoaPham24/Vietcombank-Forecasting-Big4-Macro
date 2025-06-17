#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR


df_var = df_mix.drop(columns=['Ngày'])   #Remove Day
model = VAR(df_var)
result = model.fit(maxlags=1)

# Granger
def granger_causality_table(result, variables):
    """ Granger causality tests for all variable pairs with a fixed lag """
    test_results = []
    for dependent in variables:
        for excluded in [var for var in variables if var != dependent]:
            test = result.test_causality(dependent, excluded, kind='wald')
            chi_sq = round(test.test_statistic, 4)  
            df_val = test.df  
            p_val = round(test.pvalue, 4)  
            test_results.append([dependent, excluded, chi_sq, df_val, p_val])
        test_all = result.test_causality(dependent, [var for var in variables if var != dependent], kind='wald')
        chi_sq_all = round(test_all.test_statistic, 4)
        df_all = test_all.df
        p_val_all = round(test_all.pvalue, 4)
        test_results.append([dependent, "All", chi_sq_all, df_all, p_val_all])
    return pd.DataFrame(test_results, columns=['Dependent Variable', 'Excluded', 'Chi-sq', 'df', 'Prob.'])

# Result
variables = df_var.columns
granger_table = granger_causality_table(result, variables)
print(granger_table)

