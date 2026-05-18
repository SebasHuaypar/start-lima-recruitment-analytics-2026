from supabase import create_client
from dotenv import load_dotenv
import os

# Load credentials securely from the local .env file to prevent hardcoding:
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize a global Supabase client instance to be reused by the pipeline:
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)