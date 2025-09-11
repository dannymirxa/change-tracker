import streamlit as st
from database_client import con
from modules import figure_line_by_cycle, figure_line_by_cycle_by_driver, nest_by_drivers_name, nest_by_driver_name_qcode


def show_results_timeline_page():
    # Create a row with two columns
    col1, col2 = st.columns([9, 1])  # Adjust the ratio to push the button to the right

    with col2:
        if st.button("Back to Login", key="back_to_login"):
            st.session_state['page'] = 'login'


    drivers = con.sql(f"""                        
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
                            WHERE u.username = '{st.session_state['username']}'
                            AND s.name = '{st.session_state['surveys']}'
                            QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY s.cycle, d.drivers_name
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1)
                            SELECT * FROM latest_answer 
                            order by drivers_name, cycle;
                        """).fetchall()

    qcode = con.sql(
                            f"""
                          with latest_answer AS (
                            SELECT
                            --    q.id AS question_id,
                            --    s.cycle,
                            d.drivers_name,
                                cast(regexp_extract(s.cycle, '[0-9]+', 0) as integer) as "cycle",
                                q.qcode,
                                CAST(a.answers AS INTEGER) AS answers,
                            --     a.modified_time
                            FROM answers a
                            JOIN users u      ON u.id = a.user_id
                            JOIN questions q  ON q.id = a.questions_id
                            JOIN surveys s    ON s.id = q.surveys_id
                            JOIN drivers d    ON d.id = q.drivers_id
                            WHERE u.username = '{st.session_state['username']}'
                            AND s.name = '{st.session_state['surveys']}'
                            QUALIFY ROW_NUMBER() OVER (
                                PARTITION BY s.cycle, q.qcode
                                ORDER BY a.modified_time DESC, a.id DESC
                            ) = 1)
                            SELECT * FROM latest_answer order by qcode, cycle;
                            """
                            ).fetchall()
    
    drivers_data = nest_by_drivers_name(drivers)

    qcode_data = nest_by_driver_name_qcode(qcode)
    
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