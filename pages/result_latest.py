import streamlit as st
from module.supabase_client import supabase
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, grouped_by_drivers_name_question_answers, figure_scale_by_value


def show_driver_section(driver_name, drivers_average_score_data, drivers_questions_data):
    """Display a single driver section with its metrics."""
    # Create the main expander for the driver
    with st.expander(driver_name):
        # Create and display the main figure for this driver
        data_drivers_average_score={
                item['drivers_name']: item['average_answer']
                for item in drivers_average_score_data
                if item['drivers_name'] == driver_name
             }
        fig = figure_scale_by_value(
            title=driver_name,
            data=data_drivers_average_score
        )
        st.write("Click to view detailed metrics.")
        # Generate a safe key by replacing spaces and special characters
        safe_driver_name = driver_name.replace(" ", "_").replace("&", "and")
        st.plotly_chart(fig, key=f"parent_{safe_driver_name}_latest")
        
        # Create the expander for detailed metrics
        with st.expander(f"{driver_name} Drivers"):
            data_drivers_questions = {
                        row['question']: row['answer'] 
                        for row in grouped_by_drivers_name_question_answers(drivers_questions_data)[driver_name]
                    }
            fig = figure_scale_by_value(
                title=driver_name,
                data=data_drivers_questions
            )
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key=f"child_{safe_driver_name}_latest")


def show_results_latest_page():
    # Create a row with two columns
    # Give the right column more space so the buttons appear wider
    col1, col2 = st.columns([6, 4])

    with col2:
        # Split that wider column into two equal parts for two buttons
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            if st.button("Back to Login", key="back_to_login"):
                st.session_state['page'] = 'login'
        with btn_col2:
            if st.button("Results Timeline", key="results_timeline"):
                st.session_state['page'] = 'results_timeline'

    drivers_average_score_data = supabase.rpc("get_drivers_average_score", {"username_input": f'{st.session_state['username']}'}).execute()
    drivers_questions = supabase.rpc("get_drivers_question_average_score", {"username_input": f'{st.session_state['username']}'}).execute()

    st.title(f"Change Tracker Dashboard for {st.session_state['username']} on {st.session_state['surveys_date']}")

    # List of drivers to display
    drivers = [
        "Accountability",
        "Team Leadership",
        "Business Leadership",
        "Fear & Frustration"
    ]
    
    # Display each driver section
    for driver in drivers:
        show_driver_section(driver, drivers_average_score_data.data, drivers_questions.data)