from modules import dict_to_nested_dict, list_to_dict, figure_scale_by_value

import streamlit as st
import pandas as pd
import duckdb

con = duckdb.connect('change_tracker.db')

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
                            WHERE u.username = 'john_doe'
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

"""
{
    "Business Performance": 2.67,
    "Benefits Realization": 2.29
}
"""

drivers_question_data = con.sql(
                        """
                        SELECT
                            -- q.id AS question_id,
                            d.drivers_name,
                            q.questions,
                            CAST(a.answers AS INTEGER) AS answers
                        FROM answers a
                            JOIN users u      ON u.id = a.user_id
                            JOIN questions q  ON q.id = a.questions_id
                            JOIN drivers d    ON d.id = q.drivers_id
                        WHERE u.username = 'john_doe'
                            QUALIFY ROW_NUMBER() OVER (
                            PARTITION BY q.id
                            ORDER BY a.modified_time DESC, a.id DESC
                        ) = 1
                        """
                        ).fetchall()

"""
{
    "Benefits Realization": [
        {
            "question": "Increases in revenue",
            "answer": 3
        },
        {
            "question": "Reduced costs",
            "answer": 2
        },
        {
            "question": "Better resource management",
            "answer": 3
        },
        {
            "question": "Greater team collaboration and communication",
            "answer": 3
        },
        {
            "question": "How confident are you that the performance of your Department will improve because 7-Eleven's transformation has been implemented?",
            "answer": 1
        },
        {
            "question": "Improved customer shopping experience",
            "answer": 1
        },
        {
            "question": "Better efficiency and productivity",
            "answer": 3
        }
    ],
    "Business Performance": [
        {
            "question": "Your Department's (i.e. Operations, Merchandising etc.) effectiveness",
            "answer": 1
        },
        {
            "question": "Managing costs and resources in your Team",
            "answer": 4
        },
        {
            "question": "The level of customer service (internal or external) your Team provides",
            "answer": 3
        }
    ]
}
"""


drivers_question_data = dict_to_nested_dict(drivers_question_data)


with st.expander("Business Performance"):
    fig = figure_scale_by_value(title="Business Performance", data={drivers_average_score_data[0][0]: drivers_average_score_data[0][1]})
    st.write("Click to view detailed metrics.")
    st.plotly_chart(fig, key="parent_Business_Performance")
    with st.expander("Business Performance"):
        fig = figure_scale_by_value(title="Business Performance", data=list_to_dict(drivers_question_data['Business Performance']))
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="child_Business_Performance")

with st.expander("Benefits Realization"):
    fig = figure_scale_by_value(title="Benefits Realization", data={drivers_average_score_data[1][0]: drivers_average_score_data[1][1]})
    st.write("Click to view detailed metrics.")
    st.plotly_chart(fig, key="parent_Benefits_Realization")
    with st.expander("Business Performance"):
        fig = figure_scale_by_value(title="Business Performance", data=list_to_dict(drivers_question_data['Benefits Realization']))
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="child_Benefits_Realization")

