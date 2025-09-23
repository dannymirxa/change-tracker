import os
import sys
from datetime import datetime
# Ensure the project root (parent of this script) is on sys.path so sibling modules can be imported
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from supabase import create_client, Client
from dotenv import load_dotenv
from database_client import con

load_dotenv()

supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

# response = (
#     supabase.table("surveys")
#     .select("created_time")
#     .eq("name", "Employee Satisfaction Survey")
#     .eq("cycle", "Cycle 2")
#     .limit(1)
#     .execute()
# )

response = supabase.table("questions").select("id, questions").execute().data

# surveys_date = con.sql(f"SELECT DATE(created_time) FROM surveys \
#                            WHERE name = 'Employee Satisfaction Survey' AND cycle = 'Cycle 2'\
#                            LIMIT 1" \
#                             ).fetchall()[0][0]
# print(response.data[0]['created_time'])
# print(datetime.fromisoformat(response.data[0]['created_time']).date())
print(next(item['questions'] for item in response if item["id"] == 20))
# print(username)
# print(surveys_date)