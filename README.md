# Forecasting Vietcombank Stock Prices Using VAR model: Linkages with Big4 Banks, VN-Index, and US Fed Rate
This section introduces the application of multivariate time series regression models, specifically VAR(p), to examine the relationships among variables using secondary time-series data. It also presents several techniques for achieving stationarity and selecting the appropriate model specification.

***Key words**: Stock price forecasting, VAR, financial modeling, Big4, macroeconomic impact.*
## Background
In recent years, Vietnam's banking sector has played a vital role in driving economic growth, with key players such as Vietcombank, VietinBank, BIDV, and Agribank forming the core of the so-called **"Big4"** banks. As one of the leading commercial banks in the country, Vietcombank attracts significant attention from investors, policymakers, and analysts due to its performance, stability, and influence on the broader financial market. This study uses time series data to investigate how VCB’s stock price responds to movements in peer banks, market indices, and global interest rates.

## Objectives

The objective of this project is to examine the dynamic **interrelationships between Vietcombank’s stock price and a set of influential financial and macroeconomic variables**. Using a Vector Autoregression (**VAR**) framework, the project aims to:

- Evaluate the stationarity and statistical properties of time series data;

- Determine the optimal lag structure and estimate the VAR model;

- Identify causal relationships among variables through Granger causality tests;

- Analyze how shocks in external variables affect Vietcombank’s stock price over time using Impulse Response Functions (IRFs).

This analysis provides insights into the **short-run and long-run** interactions between domestic financial performance and broader economic signals, supporting more informed decision-making for investors and policymakers.

## Data

The study utilizes secondary data in the field of finance, collected on a daily basis (excluding Saturdays, Sundays, and public holidays) during the period from **January 2, 2020 to December 31, 2024**:

| Variable                   | Symbol | Observations | Unit      | Description                                                                                         |
| -------------------------- | ------ | ------------ | --------- | --------------------------------------------------------------------------------------------------- |
| Vietcombank Stock Price    | VCB    | 1,250        | VND/share | Daily closing price of Vietcombank (VCB); the target variable for analysis and forecasting.         |
| VietinBank Stock Price     | CTS    | 1,250        | VND/share | Daily closing price of VietinBank (CTG), reflecting trends within the Big4 banking group.           |
| BIDV Stock Price           | BID    | 1,250        | VND/share | Daily closing price of BIDV (BID), representing dynamics of the Big4 banks.                         |
| Agribank Proxy Stock Price | AGR    | 1,250        | VND/share | Daily closing price used as a proxy for Agribank (AGR), part of the Big4 banks.                     |
| VN-Index                   | VNI    | 1,250        | Points    | Vietnam’s main stock market index; captures the overall trend of the local stock market.            |
| U.S. Federal Funds Rate    | FED    | 1,250        | %         | Federal Reserve’s benchmark interest rate; captures the influence of international monetary policy. |


## Framework
This project applies a 3-phase VAR-based framework—comprising data stationarity checks, model construction, and econometric analysis to examine how macro-financial factors such as Big4 bank prices, VN-Index, and the Fed rate influence Vietcombank’s stock price:

![image](https://github.com/user-attachments/assets/6b9c7563-6da8-42d6-a5d6-06e92af1c24b)
*This figure describes the framework in 3 phases*

**Note:**
![image](https://github.com/user-attachments/assets/bdcda2ce-a7d4-4a70-a57b-43614871b3c2)


## Result
The VAR model reveals significant interdependencies between Vietcombank’s stock price and macro-financial variables. Granger causality tests indicate that movements in peer banks (CTG, BID, AGR), VN-Index, and the Fed interest rate have predictive power over VCB's price dynamics. Eigenvalue stability tests confirm that the VAR system is dynamically stable. Impulse response functions (IRF) further show that shocks from VN-Index and FED rates generate clear, time-lagged impacts on VCB, suggesting market sensitivity to both domestic and international signals.

## Requirement
Ensure that you have **Python 3.8** or higher installed, then install the required Python packages:
```
# Data manipulation and computation
pandas==1.5.0
numpy==1.25.0

# Plotting
matplotlib==3.7.0

# Statistical modeling and tests
statsmodels==0.14.0

# For stationarity and Granger causality tests
scipy==1.10.0
```

## Citation
```
@book{hoang2020data,
  author    = {Huy Hoang Nguyen and Dinh Phung Tran},
  title     = {Data Analysis in Business and Economics},
  publisher = {National Economics University Publishing House},
  year      = {2020},
  note      = {Referenced from pages 43 to 57}
}
```


