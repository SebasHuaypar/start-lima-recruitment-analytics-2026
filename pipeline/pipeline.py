from extract import extract_applications
from transform import transform_applications
from normalize_data import normalize_data
from load import load_clean_data

# 1. EXTRACT: Fetch the raw JSON applications directly from the Supabase database
df = extract_applications()

# 2. TRANSFORM: Unpack the JSON answers into structured columns and calculate basic dates
clean_df = transform_applications(df)

# 3. NORMALIZE: Clean up text fields, unify aliases, and generate engagement metrics
clean_df = normalize_data(clean_df)

# 4. LOAD: Push the fully processed and sanitized dataframe back to the 'applications_clean' table
load_clean_data(clean_df)