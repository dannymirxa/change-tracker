import streamlit as st
from module.supabase_client import supabase
from database_client import con
from modules import (
    figure_line_by_cycle, 
    figure_line_by_cycle_by_driver, 
    nest_by_drivers_name, 
    grouped_by_drivers_name_cycle_answers,
    nest_by_driver_name_qcode,
    grouped_by_drivers_name_and_qcodes_cycle_answers)


def show_results_timeline_page():
    # Create a row with two columns
    col1, col2 = st.columns([9, 1])  # Adjust the ratio to push the button to the right

    with col2:
        if st.button("Back to Login", key="back_to_login"):
            st.session_state['page'] = 'login'

    drivers = supabase.rpc("get_drivers_of_user_and_survey", {"username_input": f'{st.session_state['username']}', "survey_input": f'{st.session_state['surveys']}'}).execute()

    qcode = supabase.rpc("get_qcodes_of_user_and_survey", {"username_input": f'{st.session_state['username']}', "survey_input": f'{st.session_state['surveys']}'}).execute()
    
    drivers_data = grouped_by_drivers_name_cycle_answers(drivers.data)

    qcode_data = grouped_by_drivers_name_and_qcodes_cycle_answers(qcode.data)
    
    st.title(f"Change Tracker Dashboard for {st.session_state['username']} on {st.session_state['surveys_date']}")

    driver = "Accountability"
    with st.expander(driver):
        fig = figure_line_by_cycle(
            title=driver,
            data=drivers_data[driver],
        )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Accountability_timeline")
        with st.expander(f"{driver} Drivers"):
            fig = figure_line_by_cycle_by_driver(title=driver, data=qcode_data[driver])
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Accountability_timeline")

    driver = "Team Leadership"
    with st.expander(driver):
        fig = figure_line_by_cycle(
            title=driver,
            data=drivers_data[driver],
        )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Team_Leadership_timeline")
        with st.expander(f"{driver} Drivers"):
            fig = figure_line_by_cycle_by_driver(title="Team Leadership", data=qcode_data[driver])
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Team_Leadership_timeline")

    driver = "Business Leadership"
    with st.expander(driver):
        fig = figure_line_by_cycle(
            title=driver,
            data=drivers_data[driver],
        )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Business_Leadership_timeline")
        with st.expander(f"{driver} Drivers"):
            fig = figure_line_by_cycle_by_driver(title=driver, data=qcode_data[driver])
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Leadership_timeline")

    driver = "Fear & Frustration"
    with st.expander(driver):
        fig = figure_line_by_cycle(
            title=driver,
            data=drivers_data[driver],
        )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Fear_and_Frustration_timeline")
        with st.expander(f"{driver} Drivers"):
            fig = figure_line_by_cycle_by_driver(title=driver, data=qcode_data[driver])
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Fear_and_Frustration_timeline")