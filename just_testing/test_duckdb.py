import sys
import os
import duckdb
import pandas as pd
# Ensure project root is on sys.path so local modules can be imported when running this script directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules import figure_line_by_cycle, nest_by_drivers_name

# Connect to the DuckDB database
con = duckdb.connect("change_tracker.db")


# surveys= con.sql(f"""                        
#                           with latest_answer AS (
#                             SELECT
#                             --    q.id AS question_id,
#                             --    s.cycle,
#                                 cast(regexp_extract(s.cycle, '[0-9]+', 0) as integer) as "cycle",
#                             --    d.drivers_name,
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
#                         """).fetchall()

surveys= con.sql(f"""    
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
order by drivers_name, cycle
                 
                 """).fetchall()

# print(nest_by_drivers_name(surveys))
data = nest_by_drivers_name(surveys)
driver = "Accountability"
# print({driver: dict(data)[driver]})
fig = figure_line_by_cycle(
    title=driver,
    data=dict(data)[driver],
)
# print(dict(data)[driver])

# Save a self-contained HTML file so you can open the chart in any browser.
out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "out.html"))
fig.write_html(out_path, include_plotlyjs="cdn", full_html=True)
print(f"Chart written to: {out_path}")

# Attempt to open automatically on Linux desktop environments (optional)
try:
    import subprocess
    subprocess.run(["xdg-open", out_path], check=False)
except Exception:
    pass

# Also show with the default Plotly renderer (may open a browser or display inline in some environments)
# fig.show()