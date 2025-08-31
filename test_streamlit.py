import streamlit as st
import matplotlib.pyplot as plt

# Sample data
metrics = {
    "Leadership Effectiveness": 85,
    "Issue Resolution": 70,
    "Resource Allocation": 90,
    "Team Support": 75,
    "Innovation Drive": 65
}

# Chart function
def create_chart(metrics):
    fig, ax = plt.subplots(figsize=(8, 5))
    metric_names = list(metrics.keys())
    scores = list(metrics.values())
    y_positions = range(len(metrics))

    ax.barh(y_positions, [100]*len(metrics), color="#e0e0e0", edgecolor="none")
    ax.barh(y_positions, scores, color="#4a90e2")
    for i, score in enumerate(scores):
        ax.plot(score, i, 'o', color='black')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(metric_names)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Score")
    ax.set_title("Transformation Leadership Metrics")
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    return fig

# Streamlit layout
st.title("Transformation Leadership Dashboard")

with st.expander("Leadership Effectiveness"):
    st.write("Click to view detailed metrics.")
    fig = create_chart(metrics)
    st.pyplot(fig)