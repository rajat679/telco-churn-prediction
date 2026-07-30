# Data Quality report 
## Total charges hidden missing values 

- df.isnull().sum() showed zero null values in the data, but the column's data type was actually 'str'

- total charges is a numercial column data type 'str' is not valid for it as it can cause problems in future model 

- we decided to force conversion of the column usind 'pd.to_numeric(errors ='coerce) and it revealed 11 values whic are not conversing 

- these are real missing values in the Total charges column , before altering anything  we investigated 11 rows and came to rsult that these all rows had tenure =0 meaning these all are new customers 

-fix = converted the  column to numeric and filled missing values with 0 