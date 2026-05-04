import pandas as pd
from config import supabase

def extract_submitted_applications():

    response = (
        supabase
        .table("applications_full")
        .select("*")
        .eq("status", "submitted")
        .execute()
    )

    df = pd.DataFrame(response.data)

    print(f"\nSubmitted applications: {len(df)}")

    return df