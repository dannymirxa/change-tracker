import os
# import sys
# # Ensure the project root (parent of this script) is on sys.path so sibling modules can be imported
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))