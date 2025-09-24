import os
import pandas as pd
import numpy as np

from supabase import create_client, Client
from dotenv import load_dotenv
# from database_client import con

load_dotenv()

supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

data = pd.read_csv('schema/answers.csv')

# Remove id column if present (we'll let Supabase assign it)
if 'id' in data.columns:
    data = data.drop('id', axis=1)

# JSON encoding used by the HTTP client does not accept NaN/Inf values.
# Convert NaN/Inf to None so they become SQL NULL when inserted.
data = data.replace({np.nan: None, np.inf: None, -np.inf: None})

# Optionally, if any columns should be typed (e.g. integers), convert them now.
# Example:
# if 'score' in data.columns:
#     data['score'] = pd.to_numeric(data['score'], errors='coerce').astype('Int64')

records = data.to_dict(orient='records')

# Sanity check: show how many records and whether any values remain as NaN (should be none)
print(f"Preparing to insert {len(records)} records. Any NaN left? {data.isna().any().any()}")

response = supabase.table("answers").insert(records).execute()

print(response)