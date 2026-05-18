import pandas as pd
from config import supabase

def load_clean_data(clean_df):

    # Explicitly replace Pandas 'NaN' or 'NaT' with Python 'None' for Supabase compatibility:
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

    # Loop through all columns to identify and cast any dates into standard strings for JSON:
    for col in clean_df.columns:

        if pd.api.types.is_datetime64_any_dtype(clean_df[col]):
            clean_df[col] = clean_df[col].astype(str)

        elif clean_df[col].apply(lambda x: isinstance(x, pd.Timestamp)).any():
            clean_df[col] = clean_df[col].astype(str)

        elif clean_df[col].apply(
            lambda x: hasattr(x, "isoformat") if x is not None else False
        ).any():
            clean_df[col] = clean_df[col].astype(str)

    # Convert to a list of dictionaries as required by the Supabase Python client:
    clean_data = clean_df.to_dict(orient="records")

    # Upsert the clean data into the 'applications_clean' table to update existing records:
    response = (
        supabase
        .table("applications_clean")
        .upsert(clean_data)
        .execute()
    )

    print("\nData loaded successfully!")