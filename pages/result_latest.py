import streamlit as st
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure_scale_by_value


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


    drivers_average_score_data = con.sql(f"""                        
                          WITH latest_answers AS (
                            SELECT
                                q.id AS question_id,
                                d.drivers_name,
                                CAST(a.answers AS INTEGER) AS answers
                            FROM answers a
                            JOIN users u      ON u.id = a.user_id
                            JOIN questions q  ON q.id = a.questions_id
                            JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = '{st.session_state['username']}'
                            QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY q.id
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1
                            )
                            SELECT
                            drivers_name,
                            -- COUNT(question_id) AS num_questions,
                            -- SUM(answers) AS total_answers,
                            ROUND(SUM(answers) * 1.0 / COUNT(question_id), 2) AS average_answer
                            FROM latest_answers
                            GROUP BY drivers_name;
                        """).fetchall()

    drivers_question_data = con.sql(
                            f"""
                            SELECT
                                -- q.id AS question_id,
                                d.drivers_name,
                                q.qcode,
                                CAST(a.answers AS INTEGER) AS answers
                            FROM answers a
                                JOIN users u      ON u.id = a.user_id
                                JOIN questions q  ON q.id = a.questions_id
                                JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = '{st.session_state['username']}'
                                QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY q.id
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1
                            """
                            ).fetchall()

    drivers_question_data = dict_to_nested_dict(drivers_question_data)
    
    st.title(f"Change Tracker Dashboard for {st.session_state['username']} on {st.session_state['surveys_date']}")

    driver = "Accountability"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Accountability_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Accountability_latest")

    driver = "Team Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Team_Leadership_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title="Team Leadership", data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Team_Leadership_latest")

    driver = "Business Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Business_Leadership_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Leadership_latest")

    driver = "Fear & Frustration"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Fear_and_Frustration_latest")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Fear_and_Frustration_latest")