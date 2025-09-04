import streamlit as st
import pandas as pd
import json
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure

with open("map_answers_to_scores.json", "r") as json_file:
    answers_to_scores_map = json.load(json_file)

def map_answer_with_score(map_id: int, answer: str):
    return str(answers_to_scores_map[str(map_id)][answer])

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

def show_login_page():
    st.title("Login Page")

    # Input field for the email
    email = st.text_input("Enter your email:")

    # A button to submit the login
    if st.button("Submit", key="login_submit"):
        try:
            username = con.sql(f"SELECT username FROM users WHERE email = '{email}' LIMIT 1").fetchall()[0][0]
            if username:
                st.session_state['page'] = 'welcome'
                st.session_state['username'] = username
            else:
                st.session_state['page'] = 'login'
                st.error(f"user {email} does not exist")
        except IndexError:
            st.session_state['page'] = 'login'
            st.error(f"user {email} does not exist")

def show_welcome_page():
    username = st.session_state.get('username', 'User')
    st.title(f"Welcome {username}")
    # Add further logic or components specific to the welcome page here

    if st.button("Go to Questionnaire", key="go_to_questionnaire"):
        st.session_state['page'] = 'questions'

id_questions= dict(con.sql("SELECT id, questions FROM questions;").fetchall())
questions_id= dict(con.sql("SELECT questions, id FROM questions;").fetchall())

def show_questions():
    st.title("Questions")

    """
    Business Performance
    """
    st.header("How have the following changed in the last 6 months?", divider=True)

    department_effectiveness = st.radio(
        id_questions[11],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, department_effectiveness)}")

    service_level = st.radio(
        id_questions[12],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(5, service_level)}")

    managing_costs = st.radio(
        id_questions[13],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(5, managing_costs)}")

    """
    Business Realization
    """
    st.header("Where do you see that most benefits will be delivered from ERP 2.0?", divider=True)

    team_alignment = st.radio(
        id_questions[14],
        tuple(answers_to_scores_map['6'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(6, team_alignment)}")

    time_savings = st.radio(
        id_questions[15],
        tuple(answers_to_scores_map['6'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(6, time_savings)}")

    employee_experience = st.radio(
        id_questions[16],
        tuple(answers_to_scores_map['6'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(6, employee_experience)}")

    scalable_workforce = st.radio(
        id_questions[17],
        tuple(answers_to_scores_map['6'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(6, scalable_workforce)}")

    confidence_on_performance = st.radio(
        id_questions[18],
        tuple(answers_to_scores_map['6'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(6, confidence_on_performance)}")

    # Collect user answers into a dictionary
    answers = {
        'user_id': con.sql(f"SELECT id FROM users where username = '{st.session_state.get('username')}'").fetchall()[0][0] ,  # Assuming username can serve as user_id here
        'responses': [
            {
                'question_id': questions_id[id_questions[11]],
                'answer': int(map_answer_with_score(5, department_effectiveness))
            },
            {
                'question_id': questions_id[id_questions[12]],
                'answer': int(map_answer_with_score(5, service_level))
            },
            {
                'question_id': questions_id[id_questions[13]],
                'answer': int(map_answer_with_score(5, managing_costs))
            },
            {
                'question_id': questions_id[id_questions[14]],
                'answer': int(map_answer_with_score(6, team_alignment))
            },
            {
                'question_id': questions_id[id_questions[15]],
                'answer': int(map_answer_with_score(6, time_savings))
            },
            {
                'question_id': questions_id[id_questions[16]],
                'answer': int(map_answer_with_score(6, employee_experience))
            },
            {
                'question_id': questions_id[id_questions[17]],
                'answer': int(map_answer_with_score(6, scalable_workforce))
            },
            {
                'question_id': questions_id[id_questions[18]],
                'answer': int(map_answer_with_score(6, scalable_workforce))
            }
        ]
    }

    # Show Button to Save Answers
    if st.button("Submit Answers", key="submit_answers"):
        st.session_state['page'] = 'results'
        # Convert JSON to pandas DataFrame and display
        responses_df = pd.json_normalize(answers, record_path='responses', meta='user_id')
        st.write("Answers DataFrame ready for insertion:")
        st.dataframe(responses_df)
        # Insert data from DataFrame into the DuckDB answers table
        for index, row in responses_df.iterrows():
            con.execute(
                "INSERT INTO answers (user_id, questions_id, answers) VALUES (?, ?, ?)",
                (int(row['user_id']), int(row['question_id']), row['answer'])
            )
        st.success("Responses successfully inserted into the database.")

def show_results_page():
    
    # Create a row with two columns
    col1, col2 = st.columns([9, 1])  # Adjust the ratio to push the button to the right

    with col2:
        if st.button("Back to Login", key="back_to_login"):
            st.session_state['page'] = 'login'


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
    
    st.title("Change Tracker Dashboard")

    with st.expander("Business Performance"):
        fig = figure(title="Business Performance", data={drivers_average_score_data[0][0]: drivers_average_score_data[0][1]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Business_Performance")
        with st.expander("Business Performance Drivers"):
            fig = figure(title="Business Performance", data=list_to_dict(drivers_question_data['Business Performance']))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Performance")

    with st.expander("Benefits Realization"):
        fig = figure(title="Benefits Realization", data={drivers_average_score_data[1][0]: drivers_average_score_data[1][1]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Benefits_Realization")
        with st.expander("Benefits Realization Drivers"):
            fig = figure(title="Benefits Realization", data=list_to_dict(drivers_question_data['Benefits Realization']))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Benefits_Realization")