"""
features.py — Feature engineering pipeline for Telco Customer Churn prediction.

Takes the raw CustomerChurn.csv (merged with IBM enrichment files) and produces
a model-ready dataframe: cleaned, encoded, with engineered features.

Usage:
    from features import build_features
    df_model = build_features(df_processed)
"""

import pandas as pd


def bucket_tenure(t):
    """Group raw tenure (months) into business-meaningful buckets."""
    if t <= 12:
        return 'New (0-1yr)'
    elif t <= 36:
        return 'Established (1-3yr)'
    else:
        return 'Loyal (3yr+)'


def build_features(df_processed):
    """
    Full feature engineering pipeline.

    Input: df_processed — the cleaned + merged dataframe
           (output of the Week 2 data cleaning/merging stage,
           still with human-readable categorical text values).

    Output: df_model — fully numeric, model-ready dataframe.
    """
    df = df_processed.copy()

    # --- Collapse pseudo-categories ("No internet service" / "No phone service") ---
    pseudo_category_cols = ['Online Security', 'Online Backup', 'Device Protection',
                             'Tech Support', 'Streaming TV', 'Streaming Movies']
    for col in pseudo_category_cols:
        df[col] = df[col].replace('No internet service', 'No')
    df['Multiple Lines'] = df['Multiple Lines'].replace('No phone service', 'No')

    # --- Drop columns: IDs, location raw, and leakage columns ---
    drop_cols = ['LoyaltyID', 'Customer ID', 'Zip Code',
                 'Satisfaction Score', 'Churn Category', 'Churn Reason',
                 'Dependents']  # dropping in favor of Number of Dependents

    # --- Binary encode Yes/No columns ---
    binary_cols = ['Senior Citizen', 'Partner', 'Phone Service', 'Multiple Lines',
                   'Online Security', 'Online Backup', 'Device Protection',
                   'Tech Support', 'Streaming TV', 'Streaming Movies',
                   'Paperless Billing', 'Married']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # --- One-hot encode multi-category columns ---
    multi_cat_cols = ['Internet Service', 'Contract', 'Payment Method']
    df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True)

    # --- Drop unused columns ---
    df_model = df.drop(columns=drop_cols)

    # --- Engineered feature: tenure_bucket ---
    df_model['tenure_bucket'] = df_processed['Tenure'].apply(bucket_tenure)
    df_model = pd.get_dummies(df_model, columns=['tenure_bucket'], drop_first=True)

    # --- Engineered feature: avg_monthly_spend ---
    df_model['avg_monthly_spend'] = (
        df_processed['Total Charges'] / df_processed['Tenure'].replace(0, 1)
    ).round(2)

    # --- Engineered feature: services_count ---
    service_cols = ['Online Security', 'Online Backup', 'Device Protection',
                     'Tech Support', 'Streaming TV', 'Streaming Movies']
    df_model['services_count'] = df_model[service_cols].sum(axis=1)

    return df_model