# Business Requirements Document — Telco Customer Churn Prediction

## 1. Business Context
The CFO of the company wants to know that customers will churn in the next quarter and what is main reason behind thier churn . He also wants to know the ROI of targeted retention  meaning only give discount to the customers who likely to be churn vs blanket discount  meaning give discount to all the customers .

## 2. Problem Statement

This project matters because if we can identify customers who are likely to churn before they actually leave, the company can try to retain them through targeted strategies. Acquiring a new customer is significantly more expensive than retaining an existing one, so predicting churn in advance directly reduces this cost for the business.

## 3. Data Overview
The dataset name is CustomerChurn with (7,043 rows *21 columns).We need to predict the churn . One row is basically one Customer. we have fixed the null values in total charges column as the data type of the column is 'str' and when we tried to force convert it to numeric it showed 11 null rows , we covert these rows to numeric and filled the empty rows with 0.

## 4. Key Hypotheses (to test in Week 2 EDA)
-> H1: Month-to-month contract customers will churn more  because they have no lock-in period, so leaving has zero penalty compared to someone in a 1-2 year contract.
->H2: Customers paying by mailed/electronic check will churn more than automatic payment methods  because manual payment requires active effort each month, meaning less "friction" to also cancel, whereas automatic payment is a passive habit that's easier to just... continue.
-> H3: New customers (low tenure) will churn more because they haven't yet built loyalty or gotten used to the service; the first few months are the highest-risk window before someone becomes a "settled" customer.
-> H4: Customers without add-on services (Tech Support, Online Security) will churn more  because fewer services mean fewer reasons to stay ("switching cost" is lower) and less perceived value from the subscription.

->H5: Higher Monthly Charges correlates with higher churn possibly because premium customers have higher expectations/switching incentive.
