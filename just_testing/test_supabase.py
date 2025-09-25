import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modules import dict_to_nested_dict, list_to_dict, grouped_by_drivers_name_question_answers, figure_scale_by_value
# Ensure the project root (parent of this script) is on sys.path so sibling modules can be imported

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

# response = supabase.table("questions").select("id, questions").execute().data

# surveys_date = con.sql(f"SELECT DATE(created_time) FROM surveys \
#                            WHERE name = 'Employee Satisfaction Survey' AND cycle = 'Cycle 2'\
#                            LIMIT 1" \
#                             ).fetchall()[0][0]
# print(response.data[0]['created_time'])
# print(datetime.fromisoformat(response.data[0]['created_time']).date())
# print(next(item['questions'] for item in response if item["id"] == 20))
# print(username)
# print(surveys_date)


# Insert into Supabase
# response = supabase.rpc("get_drivers_average_score", {"username_input": 'john_doe'}).execute()
# response = supabase.rpc("get_qcodes_of_user_and_survey", {"username_input": 'john_doe', "survey_input": 'Employee Satisfaction Survey'}).execute()
response = supabase.rpc("get_drivers_question_average_score", {"username_input": 'john_doe'}).execute()
data_drivers_questions = {
                        row['question']: row['answer'] 
                        for row in grouped_by_drivers_name_question_answers(response.data)['Accountability']
                    }
print(response.data)
print(grouped_by_drivers_name_question_answers(response.data))
# print(data_drivers_questions)
print()
# drivers_question_data = con.sql(
#                             f"""
#                             SELECT
#                                 -- q.id AS question_id,
#                                 d.drivers_name,
#                                 q.qcode,
#                                 CAST(a.answers AS INTEGER) AS answers
#                             FROM answers a
#                                 JOIN users u      ON u.id = a.user_id
#                                 JOIN questions q  ON q.id = a.questions_id
#                                 JOIN drivers d    ON d.id = q.drivers_id
#                             WHERE u.username = 'john_doe'
#                                 QUALIFY ROW_NUMBER() OVER (
#                                 PARTITION BY q.id
#                                 ORDER BY a.modified_time DESC, a.id DESC
#                             ) = 1
#                             """
#                             ).fetchall()

# print(drivers_question_data)

# drivers_question_data = dict_to_nested_dict(drivers_question_data)
# print()
# print(drivers_question_data)