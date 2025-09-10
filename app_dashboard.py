import streamlit as st
import plotly.express as px
import pandas as pd
import json
from io import StringIO
from datetime import datetime, timedelta

# Set page config
st.set_page_config(layout="wide", page_title="XM Dashboard")

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 20px;
        margin-bottom: 20px;
    }
    .kpi-card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        background-color: #f9f9f9;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10px;
        height: 100%;
    }
    .kpi-value {
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
    }
    .kpi-label {
        font-size: 0.9rem;
        color: #555;
        margin: 0;
    }
    .sidebar {
        background-color: #f5f5f5;
        padding: 20px;
        border-right: 1px solid #ddd;
    }
    .search-box {
        width: 100%;
        padding: 10px;
        margin: 15px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
    }
    .recently-visited {
        margin-top: 20px;
    }
    .project-item {
        padding: 15px 0;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .project-name {
        font-weight: 500;
        margin: 0;
    }
    .project-type {
        font-size: 0.9rem;
        color: #777;
        margin: 0;
    }
    .project-responses {
        font-size: 0.85rem;
        color: #777;
    }
    .status-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-left: 10px;
    }
    .active {
        background-color: #e8f5e8;
        color: #2e7d32;
    }
    .button {
        padding: 8px 16px;
        border: 1px solid #3b82f6;
        background-color: white;
        color: #3b82f6;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        text-decoration: none;
        margin-right: 10px;
        margin-bottom: 10px;
    }
    .button:hover {
        background-color: #3b82f6;
        color: white;
    }
    .link {
        color: #3b82f6;
        text-decoration: none;
        font-size: 0.9rem;
    }
    .link:hover {
        text-decoration: underline;
    }
    .upload-buttons {
        margin-top: 20px;
        text-align: center;
    }
    /* Reduce Gantt chart height and adjust margins */
    .gantt-chart {
        height: 400px;
        margin: 0; /* Remove default margin */
        padding: 0; /* Remove default padding */
    }
    /* Style the chart title to be closer to the bars */
    .gantt-chart .plotly-title {
        margin-bottom: 10px !important; /* Reduce space below title */
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for data
if 'recently_visited_data' not in st.session_state:
    st.session_state.recently_visited_data = [
        {"name": "Appointment Scheduling", "type": "Survey", "responses": "16 Responses", "status": "Active"},
        {"name": "Customer Satisfaction Survey", "type": "Survey", "responses": "2 Responses", "status": "Active"},
        {"name": "Customer Dashboards", "type": "Dashboards", "responses": "15 Dashboards", "status": "Active"}
    ]

if 'workflows_summary_data' not in st.session_state:
    st.session_state.workflows_summary_data = {
        "active_workflows": 12,
        "completed_workflows": 3,
        "failed_workflows": 0
    }

# Initialize session state for Gantt data
if 'tickets_gantt_data' not in st.session_state:
    st.session_state.tickets_gantt_data = [
        {"Task": "Fix login bug", "Start": "2023-10-01", "Finish": "2023-10-03", "Assignee": "Alex"},
        {"Task": "Update API docs", "Start": "2023-10-02", "Finish": "2023-10-05", "Assignee": "Sam"},
        {"Task": "Performance review", "Start": "2023-10-03", "Finish": "2023-10-06", "Assignee": "Jordan"},
        {"Task": "Security patch", "Start": "2023-10-04", "Finish": "2023-10-08", "Assignee": "Alex"},
        {"Task": "Feature request A", "Start": "2023-10-05", "Finish": "2023-10-10", "Assignee": "Taylor"}
    ]

# Function to parse JSON data
def parse_json_data(uploaded_file, data_type):
    try:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        data = json.load(stringio)
        return data
    except Exception as e:
        st.error(f"Error parsing {data_type} JSON: {str(e)}")
        return None

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/40x40?text=XM", width=40)
    st.write("Welcome to XM")
    st.write("")
    st.write(" ")
    st.write(" ")

    # Search bar
    search = st.text_input("Search by name, type, owner...", placeholder="Search...")
    
    # Recently visited
    st.markdown("<h4>Recently visited</h4>", unsafe_allow_html=True)
    st.markdown('<a href="#" class="link">See all projects</a>', unsafe_allow_html=True)
    
    # Projects
    for p in st.session_state.recently_visited_data:
        st.markdown(f"""
            <div class="project-item">
                <div>
                    <p class="project-name">{p['name']}</p>
                    <p class="project-type">{p['type']}</p>
                    <p class="project-responses'>{p['responses']}</p>
                </div>
                <span class="status-badge active">{p['status']}</span>
            </div>
        """, unsafe_allow_html=True)

    # Upload buttons
    st.markdown("<div class='upload-buttons'>", unsafe_allow_html=True)
    st.markdown("<h4>Upload Configuration</h4>", unsafe_allow_html=True)
    
    # File uploaders
    recently_visited_file = st.file_uploader("Upload Recently Visited JSON", type="json", key="recently_visited")
    workflows_summary_file = st.file_uploader("Upload Workflows Summary JSON", type="json", key="workflows_summary")
    tickets_gantt_file = st.file_uploader("Upload Tickets Gantt JSON", type="json", key="tickets_gantt")
    
    # Process uploaded files
    if recently_visited_file:
        data = parse_json_data(recently_visited_file, "Recently Visited")
        st.session_state.recently_visited_data = data
        st.success("Recently Visited data updated!")

    if workflows_summary_file:
        data = parse_json_data(workflows_summary_file, "Workflows Summary")
        st.session_state.workflows_summary_data = data
        st.success("Workflows Summary data updated!")

    if tickets_gantt_file:
        data = parse_json_data(tickets_gantt_file, "Tickets Gantt")
        if data and isinstance(data, list) and len(data) > 0 and all(isinstance(item, dict) for item in data):
            # Basic validation: check if required keys are present in the first item
            required_keys = {"Task", "Start", "Finish"}
            if required_keys.issubset(set(data[0].keys())):
                st.session_state.tickets_gantt_data = data
                st.success("Tickets Gantt data updated!")
            else:
                st.error("Invalid Gantt JSON: Missing required keys (Task, Start, Finish)")
        elif data:
            st.error("Invalid Gantt JSON: Data must be a list of objects")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Main content
st.title("Home")

# Top KPIs - Workflows Summary
st.markdown("<h3>Your workflows summary</h3>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='kpi-card'><p class='kpi-label'>Your active workflows</p><p class='kpi-value'>{st.session_state.workflows_summary_data['active_workflows']}</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='kpi-card'><p class='kpi-label'>Completed (last 72 hours)</p><p class='kpi-value'>{st.session_state.workflows_summary_data['completed_workflows']}</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='kpi-card'><p class='kpi-label'>Failed (last 72 hours)</p><p class='kpi-value' style='color: #d32f2f;'>{st.session_state.workflows_summary_data['failed_workflows']}</p></div>", unsafe_allow_html=True)

# Action buttons
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<a href="#" class="link">View run history</a>', unsafe_allow_html=True)
with col2:
    st.button("Create a workflow", key="create_workflow")

# Tickets Summary Section - Replaced with Gantt Chart
st.markdown("<h3>Tickets summary</h3>", unsafe_allow_html=True)

# Convert session state data to DataFrame
try:
    gantt_df = pd.DataFrame(st.session_state.tickets_gantt_data)
    # Ensure Start and Finish columns are datetime
    gantt_df['Start'] = pd.to_datetime(gantt_df['Start'])
    gantt_df['Finish'] = pd.to_datetime(gantt_df['Finish'])
    
    # Create Gantt chart
    fig = px.timeline(
        gantt_df, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Assignee" if "Assignee" in gantt_df.columns else None,
        title="Current Tickets Timeline"
    )

    # Improve layout
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Tickets",
        legend_title="Assignee" if "Assignee" in gantt_df.columns else None,
        margin=dict(l=20, r=20, t=20, b=20), # Reduced top margin
        height=400 # Set a fixed height
    )

    # Display the chart in a container with custom class for styling
    st.markdown('<div class="gantt-chart">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
except Exception as e:
    st.error(f"Error creating Gantt chart: {str(e)}")
    # Fallback to sample data if there's an error
    st.markdown('<div class="gantt-chart">', unsafe_allow_html=True)
    st.warning("Displaying sample data due to configuration error.")
    
    # Generate sample data for fallback
    fallback_data = [
        {"Task": "Fallback Task 1", "Start": "2023-10-01", "Finish": "2023-10-03", "Assignee": "System"},
        {"Task": "Fallback Task 2", "Start": "2023-10-02", "Finish": "2023-10-05", "Assignee": "System"}
    ]
    fallback_df = pd.DataFrame(fallback_data)
    fallback_df['Start'] = pd.to_datetime(fallback_df['Start'])
    fallback_df['Finish'] = pd.to_datetime(fallback_df['Finish'])
    
    fallback_fig = px.timeline(
        fallback_df, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Assignee",
        title="Fallback Tickets Timeline"
    )
    fallback_fig.update_yaxes(autorange="reversed")
    fallback_fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        height=400
    )
    st.plotly_chart(fallback_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# View all tickets link
st.markdown('<div style="text-align: right; margin-top: -20px;"><a href="#" class="link">View all tickets</a></div>', unsafe_allow_html=True)