# Data Quality report 
## Total charges hidden missing values 

- df.isnull().sum() showed zero null values in the data, but the column's data type was actually 'str'

- total charges is a numercial column data type 'str' is not valid for it as it can cause problems in future model 

- we decided to force conversion of the column usind 'pd.to_numeric(errors ='coerce) and it revealed 11 values whic are not conversing 

- these are real missing values in the Total charges column , before altering anything  we investigated 11 rows and came to rsult that these all rows had tenure =0 meaning these all are new customers 

-fix = converted the  column to numeric and filled missing values with 0 


## Issue: Data leakage in Satisfaction Score, Churn Category, Churn Reason

- Satisfaction Score showed a near-perfect churn split: churners scored 1-3 
  (mean 1.74), non-churners scored 3-5 (mean 3.79), with essentially zero overlap.
- This is a sign the score was likely captured at/after the churn event, not 
  before it — meaning it reflects the outcome rather than predicting it.
- Decision: exclude Satisfaction Score, Churn Category, and Churn Reason from 
  model input features (Week 3+). Retained for Week 5 explainability narrative only.
- Verified CLTV does NOT show this pattern (overlapping distributions, modest 
  mean difference: 4491 vs 4149) - safe to use as a feature.