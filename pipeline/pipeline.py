from extract import extract_applications
from transform import transform_applications
from normalize import normalize_data
from load import load_clean_data

# Extract
df = extract_applications()

# Transform
clean_df = transform_applications(df)

# Normalize
clean_df = normalize_data(clean_df)

# Load
load_clean_data(clean_df)