import duckdb

# Connect to the DuckDB database
con = duckdb.connect("change_tracker.db")


surveys= con.sql("SELECT DATE(created_time) FROM surveys where name = 'Employee Satisfaction Survey';").fetchall()[0][0]
# print(id_questions[1])

# questions_id= dict(con.sql("SELECT questions, id FROM questions;").fetchall())
# # print(questions_id[id_questions[1]])

# metrics_data = con.sql("""SELECT q.questions, cast(a.answers as INTEGER) answers, a.created_time, a.modified_time  FROM answers a
#                         INNER JOIN users u on u.id = a.user_id
#                         INNER JOIN questions q on q.id = a.questions_id
#                         INNER JOIN drivers d on d.id = q.drivers_id
#                         WHERE 1=1
#                         AND u.username = 'john_doe'
#                         AND d.drivers_name = 'Business Performance'
#                         ;""").fetchall()

print(surveys)