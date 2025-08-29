import streamlit as st
import duckdb
import json
import pandas as pd

# Connect to the DuckDB database
con = duckdb.connect("change_tracker.db")

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


def show_questions():
    st.title("Questions")

    st.header("How have the following changed in the last 6 months?", divider=True)
    # Example question about department's effectiveness
    department_effectiveness = st.radio(
        "Your Department's (i.e. Operations, Merchandising etc.) effectiveness",
        ('Very Effective', 'Effective', 'Neutral', 'Ineffective', 'Very Ineffective'),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, department_effectiveness)}")


    # Question about customer service level
    customer_service_level = st.radio(
        "The level of customer service (internal or external) your Team provides",
        ('Excellent', 'Good', 'Average', 'Below Average', 'Poor'),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(2, customer_service_level)}")

    # Question about managing costs and resources
    managing_costs = st.radio(
        "Managing costs and resources in your Team",
        ('Very Efficient', 'Efficient', 'Neutral', 'Inefficient', 'Very Inefficient'),
        horizontal=True
    )

    st.write(f"Your gave score: {map_answer_with_score(3, managing_costs)}")

    # Collect user answers into a dictionary
    answers = {
        'user_id': con.sql(f"SELECT id FROM users where username = '{st.session_state.get('username')}'").fetchall()[0][0] ,  # Assuming username can serve as user_id here
        'responses': [
            {
                'question_id': con.sql("SELECT id FROM questions WHERE questions = 'Your Department''s (i.e. Operations, Merchandising etc.) effectiveness'").fetchall()[0][0],
                'answer': int(map_answer_with_score(1, department_effectiveness))
            },
            {
                'question_id': con.sql("SELECT id FROM questions WHERE questions = 'The level of customer service (internal or external) your Team provides'").fetchall()[0][0],
                'answer': int(map_answer_with_score(2, customer_service_level))
            },
            {
                'question_id': con.sql("SELECT id FROM questions WHERE questions = 'Managing costs and resources in your Team'").fetchall()[0][0],
                'answer': int(map_answer_with_score(3, managing_costs))
            }
        ]
    }

    # Show Button to Save Answers
    if st.button("Submit Answers", key="submit_answers"):
        answers_json = json.dumps(answers)
        # Convert JSON to pandas DataFrame and display
        responses_df = pd.json_normalize(answers, record_path='responses', meta='user_id')
        st.write("Answers DataFrame ready for insertion:")
        st.dataframe(responses_df)
        # Insert data from DataFrame into the DuckDB answers table
        for index, row in responses_df.iterrows():
            con.execute(
                "INSERT INTO answers (user_id, questions_id, answers) VALUES (?, ?, ?)",
                (row['user_id'], row['question_id'], row['answer'])
            )
        st.success("Responses successfully inserted into the database.")

# Control page navigation
def navigate_pages():
    if st.session_state['page'] == 'login':
        show_login_page()
    elif st.session_state['page'] == 'welcome':
        show_welcome_page()
    elif st.session_state['page'] == 'questions':
        show_questions()

navigate_pages()