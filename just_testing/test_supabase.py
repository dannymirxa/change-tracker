import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modules import dict_to_nested_dict, list_to_dict, figure_scale_by_value, nest_by_drivers_name, nest_by_driver_name_qcode, grouped_by_drivers_name_cycle_answers, grouped_by_drivers_name_and_qcodes_cycle_answers
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
response = supabase.rpc("get_drivers_of_user_and_survey", {"username_input": 'john_doe', "survey_input": 'Employee Satisfaction Survey'}).execute()

# drivers_average_score_data = con.sql(f"""                        
#                         WITH latest_answers AS (
#                         SELECT
#                             q.id AS question_id,
#                             d.drivers_name,
#                             CAST(a.answers AS INTEGER) AS answers
#                         FROM answers a
#                         JOIN users u      ON u.id = a.user_id
#                         JOIN questions q  ON q.id = a.questions_id
#                         JOIN drivers d    ON d.id = q.drivers_id
#                         WHERE u.username = 'john_doe'
#                         QUALIFY ROW_NUMBER() OVER (
#                             PARTITION BY q.id
#                             ORDER BY a.modified_time DESC, a.id DESC
#                         ) = 1
#                         )
#                         SELECT
#                         drivers_name,
#                         -- COUNT(question_id) AS num_questions,
#                         -- SUM(answers) AS total_answers,
#                         ROUND(SUM(answers) * 1.0 / COUNT(question_id), 2) AS average_answer
#                         FROM latest_answers
#                         GROUP BY drivers_name;
#                     """).fetchall()

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

drivers = con.sql(f"""                        
                            with latest_answer AS (
                            SELECT
                            --    q.id AS question_id,
                                cast(regexp_extract(s.cycle, '[0-9]+', 0) as integer) as "cycle",
                                d.drivers_name,
                            --    q.qcode,
                                CAST(a.answers AS INTEGER) AS answers,
                            --    a.modified_time
                            FROM answers a
                            JOIN users u      ON u.id = a.user_id
                            JOIN questions q  ON q.id = a.questions_id
                            JOIN surveys s    ON s.id = q.surveys_id
                            JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = 'john_doe'
                            AND s.name = 'Employee Satisfaction Survey'
                            QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY s.cycle, d.drivers_name
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1)
                            SELECT * FROM latest_answer 
                            order by drivers_name, cycle;
                        """).fetchall()

# qcode = con.sql(
#                             f"""
#                           with latest_answer AS (
#                             SELECT
#                             --    q.id AS question_id,
#                             --    s.cycle,
#                             d.drivers_name,
#                                 cast(regexp_extract(s.cycle, '[0-9]+', 0) as integer) as "cycle",
#                                 q.qcode,
#                                 CAST(a.answers AS INTEGER) AS answers,
#                             --     a.modified_time
#                             FROM answers a
#                             JOIN users u      ON u.id = a.user_id
#                             JOIN questions q  ON q.id = a.questions_id
#                             JOIN surveys s    ON s.id = q.surveys_id
#                             JOIN drivers d    ON d.id = q.drivers_id
#                             WHERE u.username = 'john_doe'
#                             AND s.name = 'Employee Satisfaction Survey'
#                             QUALIFY ROW_NUMBER() OVER (
#                                 PARTITION BY s.cycle, q.qcode
#                                 ORDER BY a.modified_time DESC, a.id DESC
#                             ) = 1)
#                             SELECT * FROM latest_answer order by qcode, cycle;
#                             """
#                             ).fetchall()

# qcode_data = nest_by_driver_name_qcode(qcode)
# print(qcode_data)
print(grouped_by_drivers_name_cycle_answers(response.data))
print()
print(nest_by_drivers_name(drivers))

# print(drivers_question_data)
# print("-----")

# print( response.data)
# print([tuple(data.values()) for data in response.data])

driver = "Accountability"
# print({
#     item['drivers_name']: item['average_answer']
#     for item in response.data
#     if item['drivers_name'] == driver
# }
# )
# print("-----")
# drivers_question_data = dict_to_nested_dict(drivers_question_data)
# print(drivers_question_data)
# print("-----")
# print(list_to_dict(drivers_question_data[driver]))
print()
# print(grouped_by_drivers_name_and_qcodes_cycle_answers(response.data))

from collections import defaultdict

# def grouped_by_drivers_name(data: dict) -> dict:
#     grouped = defaultdict(list)
#     for item in data:
#         grouped[item['drivers_name']].append({
#             "cycle": item['cycle'],
#             "answer": item['answers']
#         })
#     return dict(grouped)

# print(grouped_by_drivers_name(response.data))
# drivers_data = nest_by_drivers_name(drivers)
# print(drivers_data)

# print(grouped_by_drivers_name(response.data))
# print("-----")
# print(dict_to_nested_dict([tuple(data.values()) for data in response.data]))
# print(list_to_dict(grouped_by_drivers_name(response.data)[driver]))
# print("-----")
# print({row['question']: row['answer'] for row in grouped_by_drivers_name(response.data)[driver]})


# print({driver: dict(drivers_average_score_data)[driver]})
