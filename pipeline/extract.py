import pandas as pd
from config import supabase

def extract_applications():

    # Fetch all raw application records directly from the Supabase database:
    response = (
        supabase
        .table("applications")
        .select("*")
        .execute()
    )

    # Convert the JSON response data into a Pandas DataFrame for easier manipulation
    df = pd.DataFrame(response.data)

    print(f"\nTotal applications: {len(df)}")

    return df