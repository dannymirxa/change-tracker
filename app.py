import streamlit as st
import duckdb
import json
import pandas as pd
import matplotlib.pyplot as plt

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

# Chart function
def create_chart(metrics):
    fig, ax = plt.subplots(figsize=(8, 5))
    metric_names = list(dict(metrics).keys())
    scores = list(dict(metrics).values())
    y_positions = range(len(metrics))

    ax.barh(y_positions, [5]*len(metrics), color="#e0e0e0", edgecolor="none")
    ax.barh(y_positions, scores, color="#4a90e2")
    for i, score in enumerate(scores):
        ax.plot(score, i, 'o', color='black')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(metric_names)
    ax.invert_yaxis()
    ax.set_xlim(0, 5)
    ax.set_xlabel("Score")
    ax.set_title("Transformation Leadership Metrics")
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    return fig

def show_results_page():


# Control page navigation
def navigate_pages():
    if st.session_state['page'] == 'login':
        show_login_page()
    elif st.session_state['page'] == 'welcome':
        show_welcome_page()
    elif st.session_state['page'] == 'questions':
        show_questions()
    elif st.session_state['page'] == 'results':
        show_results_page()

navigate_pages()