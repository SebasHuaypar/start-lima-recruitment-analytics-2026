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

    # Convert date/datetime columns to string
    for col in clean_df.columns:

        if pd.api.types.is_datetime64_any_dtype(clean_df[col]):
            clean_df[col] = clean_df[col].astype(str)

        elif clean_df[col].apply(lambda x: isinstance(x, pd.Timestamp)).any():
            clean_df[col] = clean_df[col].astype(str)

        elif clean_df[col].apply(
            lambda x: hasattr(x, "isoformat") if x is not None else False
        ).any():
            clean_df[col] = clean_df[col].astype(str)

    # Convert dataframe to dictionary
    clean_data = clean_df.to_dict(orient="records")

    # Load data into Supabase
    response = (
        supabase
        .table("applications_clean")
        .upsert(clean_data)
        .execute()
    )

    print("\nData loaded successfully!")