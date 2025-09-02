import streamlit as st
import pandas as pd
import json
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure

with open("map_business_performance_scores.json", "r") as json_file:
    business_performance_scores_map = json.load(json_file)

def map_answer_with_score(question_id: int, answer: str):
    return str(business_performance_scores_map[str(question_id)][answer])

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

    st.header("How have the following changed in the last 6 months?", divider=True)
    # Example question about department's effectiveness
    department_effectiveness = st.radio(
        id_questions[1],
        ('Very Effective', 'Effective', 'Neutral', 'Ineffective', 'Very Ineffective'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, department_effectiveness)}")


    # Question about customer service level
    customer_service_level = st.radio(
        id_questions[2],
        ('Excellent', 'Good', 'Average', 'Below Average', 'Poor'),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(2, customer_service_level)}")

    # Question about managing costs and resources
    managing_costs = st.radio(
        id_questions[3],
        ('Very Efficient', 'Efficient', 'Neutral', 'Inefficient', 'Very Inefficient'),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(3, managing_costs)}")

    st.header("Where do you see that most benefits will be delivered from 7-Eleven's transformation to be the best retailer of convenience?", divider=True)

    increases_in_revenue = st.radio(
        id_questions[4],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, increases_in_revenue)}")

    reduced_cost = st.radio(
        id_questions[5],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, reduced_cost)}")

    customer_shopping_experience = st.radio(
        id_questions[6],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, customer_shopping_experience)}")

    efficiency_and_productivity = st.radio(
        id_questions[7],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, efficiency_and_productivity)}")

    collaboration_and_communication = st.radio(
        id_questions[8],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, collaboration_and_communication)}")

    resource_management = st.radio(
        id_questions[9],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, resource_management)}")

    confident_improvement = st.radio(
        id_questions[10],
        ('Not at all', 'Bad', 'Moderate', 'Good', 'Considerable'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, confident_improvement)}")

    # Collect user answers into a dictionary
    answers = {
        'user_id': con.sql(f"SELECT id FROM users where username = '{st.session_state.get('username')}'").fetchall()[0][0] ,  # Assuming username can serve as user_id here
        'responses': [
            {
                'question_id': questions_id[id_questions[1]],
                'answer': int(map_answer_with_score(1, department_effectiveness))
            },
            {
                'question_id': questions_id[id_questions[2]],
                'answer': int(map_answer_with_score(2, customer_service_level))
            },
            {
                'question_id': questions_id[id_questions[3]],
                'answer': int(map_answer_with_score(3, managing_costs))
            },
            {
                'question_id': questions_id[id_questions[4]],
                'answer': int(map_answer_with_score(4, increases_in_revenue))
            },
            {
                'question_id': questions_id[id_questions[5]],
                'answer': int(map_answer_with_score(4, reduced_cost))
            },
            {
                'question_id': questions_id[id_questions[6]],
                'answer': int(map_answer_with_score(4, customer_shopping_experience))
            },
            {
                'question_id': questions_id[id_questions[7]],
                'answer': int(map_answer_with_score(4, efficiency_and_productivity))
            },
            {
                'question_id': questions_id[id_questions[8]],
                'answer': int(map_answer_with_score(4, efficiency_and_productivity))
            },
            {
                'question_id': questions_id[id_questions[9]],
                'answer': int(map_answer_with_score(4, resource_management))
            },
            {
                'question_id': questions_id[id_questions[10]],
                'answer': int(map_answer_with_score(4, confident_improvement))
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
                                q.questions,
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
        with st.expander("Business Performance"):
            fig = figure(title="Business Performance", data=list_to_dict(drivers_question_data['Business Performance']))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Performance")

    with st.expander("Benefits Realization"):
        fig = figure(title="Benefits Realization", data={drivers_average_score_data[1][0]: drivers_average_score_data[1][1]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Benefits_Realization")
        with st.expander("Business Performance"):
            fig = figure(title="Business Performance", data=list_to_dict(drivers_question_data['Benefits Realization']))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Benefits_Realization")