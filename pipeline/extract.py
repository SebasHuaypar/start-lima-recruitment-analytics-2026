import pandas as pd
from config import supabase

def extract_submitted_applications():

    response = (
        supabase
        .table("applications")
        .select("*")
        .execute()
    )

    df = pd.DataFrame(response.data)

    print(f"\nTotal applications: {len(df)}")

    return df