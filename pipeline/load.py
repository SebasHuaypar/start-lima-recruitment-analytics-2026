import pandas as pd
from config import supabase

def load_clean_data(clean_df):

    # Handle nulls and inf values
    clean_df = (
        clean_df
        .replace({pd.NA: None})
        .replace([float("inf"), float("-inf")], None)
    )

    clean_df = (
        clean_df
        .astype(object)
        .where(pd.notnull(clean_df), None)
    )

    print(clean_df.isna().sum())

    clean_data = clean_df.to_dict(orient="records")

    response = (
        supabase
        .table("applications_clean")
        .upsert(clean_data)
        .execute()
    )

    print("\nData loaded successfully!")