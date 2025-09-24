import streamlit as st
from module.supabase_client import supabase
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, grouped_by_drivers_name_question_answers, figure_scale_by_value


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

    drivers_questions = supabase.rpc("get_drivers_question", {"username_input": 'john_doe'}).execute()

    st.title(f"Change Tracker Dashboard for {st.session_state['username']} on {st.session_state['surveys_date']}")

    driver = "Accountability"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={
                                                            item['drivers_name']: item['average_answer']
                                                            for item in drivers_average_score_data.data
                                                            if item['drivers_name'] == driver
                                                        }
                                    )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Accountability_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data={row['question']: row['answer'] for row in grouped_by_drivers_name_question_answers(drivers_questions.data)[driver]})
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Accountability_latest")

    driver = "Team Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={
                                                            item['drivers_name']: item['average_answer']
                                                            for item in drivers_average_score_data.data
                                                            if item['drivers_name'] == driver
                                                        }
                                    )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Team_Leadership_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title="Team Leadership", data={row['question']: row['answer'] for row in grouped_by_drivers_name_question_answers(drivers_questions.data)[driver]})
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Team_Leadership_latest")

    driver = "Business Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={
                                                            item['drivers_name']: item['average_answer']
                                                            for item in drivers_average_score_data.data
                                                            if item['drivers_name'] == driver
                                                        }
                                    )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Business_Leadership_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data={row['question']: row['answer'] for row in grouped_by_drivers_name_question_answers(drivers_questions.data)[driver]})
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Leadership_latest")

    driver = "Fear & Frustration"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={
                                                            item['drivers_name']: item['average_answer']
                                                            for item in drivers_average_score_data.data
                                                            if item['drivers_name'] == driver
                                                        }
                                    )
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Fear_and_Frustration_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data={row['question']: row['answer'] for row in grouped_by_drivers_name_question_answers(drivers_questions.data)[driver]})
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Fear_and_Frustration_latest")