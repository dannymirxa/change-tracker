
import matplotlib.pyplot as plt
import duckdb

con = duckdb.connect('change_tracker.db')

metrics_data = con.sql("""SELECT q.questions, cast(a.answers as INTEGER) answers FROM answers a
                        INNER JOIN users u on u.id = a.user_id
                        INNER JOIN questions q on q.id = a.questions_id
                        INNER JOIN drivers d on d.id = q.drivers_id
                        WHERE 1=1
                        AND u.username = 'john_doe'
                        AND d.drivers_name = 'Business Performance'
                        ;""").fetchall()

print(dict(metrics_data))

# Chart function
def create_chart(metrics):
    fig, ax = plt.subplots(figsize=(8, 5))
    metric_names = list(dict(metrics).keys())
    scores = list(dict(metrics).values())
    y_positions = range(len(metrics))

    ax.barh(y_positions, [5]*len(metrics), color="#e0e0e0", edgecolor="none")
    ax.barh(y_positions, scores, color="#4a90e2")
    for i, score in enumerate(scores):
        ax.plot(score, i, 'o', color='black')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(metric_names)
    ax.invert_yaxis()
    ax.set_xlim(0, 5)
    ax.set_xlabel("Score")
    ax.set_title("Transformation Leadership Metrics")
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    return fig

# print(dict(metrics_data).keys())

# # Create the chart using the dictionary
fig = create_chart(metrics_data)

# Display the chart
plt.show()