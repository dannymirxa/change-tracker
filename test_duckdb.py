import duckdb

# Connect to the DuckDB database
con = duckdb.connect("change_tracker.db")


id_questions= dict(con.sql("SELECT id, questions FROM questions;").fetchall())
print(id_questions[1])

questions_id= dict(con.sql("SELECT questions, id FROM questions;").fetchall())
print(questions_id[id_questions[1]])