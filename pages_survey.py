import streamlit as st
import pandas as pd
import json
from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure_scale_by_value

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
    Accountability
    """
    st.header("Accountability", divider=True)

    llb_role_clarity = st.radio(
        id_questions[19],
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_role_clarity)}")
    
    # Add a text area for user comments
    llb_role_clarity_comment = st.text_area("Comments:", key="role_clarity_comment")
    
    llb_accountable = st.radio(
        id_questions[20],
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_accountable)}")
    
    # Add a text area for user comments
    llb_accountable_comment = st.text_area("Comments:", key="accountable_comment")
    
    llb_objectives_outcomes = st.radio(
        id_questions[21],
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_objectives_outcomes)}")
    
    # Add a text area for user comments
    llb_objectives_outcomes_comment = st.text_area("Comments:", key="objectives_outcomes_comment")

    """
    Team Leadership
    """
    st.header("Team Leadership", divider=True)

    llb_leads_implementation = st.radio(
        id_questions[22],
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_leads_implementation)}")

    llb_performance_management = st.radio(
        id_questions[23],
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_performance_management)}")

    llb_talents_utilised = st.radio(
        id_questions[24],
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_talents_utilised)}")

    llb_conf_lv5_ldr = st.radio(
        id_questions[25],
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_conf_lv5_ldr)}")

    llb_recognised_rewarded = st.radio(
        id_questions[26],
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_recognised_rewarded)}")

    """
    Business Leadership
    """
    st.header("Business Leadership", divider=True)

    enb_ldr_support_system = st.radio(
        id_questions[27],
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, enb_ldr_support_system)}")

    enb_ldr_time_resources = st.radio(
        id_questions[28],
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, enb_ldr_time_resources)}")

    enb_conf_lv2_ldr = st.radio(
        id_questions[29],
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, enb_conf_lv2_ldr)}")

    sfb_current_change_mgmt = st.radio(
        id_questions[30],
        tuple(answers_to_scores_map['4'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, sfb_current_change_mgmt)}")

    rsb_quick_remedial = st.radio(
        id_questions[31],
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, rsb_quick_remedial)}")

    """
    Fear and Frustration
    """
    st.header("Fear and Frustration", divider=True)

    eeb_fear = st.radio(
        id_questions[32],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_fear)}")

    eeb_distress = st.radio(
        id_questions[33],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_distress)}")

    eeb_anger = st.radio(
        id_questions[34],
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_anger)}")

    # Collect user answers into a dictionary
    answers = {
        'user_id': con.sql(f"SELECT id FROM users where username = '{st.session_state.get('username')}'").fetchall()[0][0] ,  # Assuming username can serve as user_id here
        'responses': [
            {
                'question_id': questions_id[id_questions[19]],
                'answer': int(map_answer_with_score(1, llb_role_clarity))
            },
            {
                'question_id': questions_id[id_questions[20]],
                'answer': int(map_answer_with_score(1, llb_accountable))
            },
            {
                'question_id': questions_id[id_questions[21]],
                'answer': int(map_answer_with_score(1,  llb_objectives_outcomes))
            },
            {
                'question_id': questions_id[id_questions[22]],
                'answer': int(map_answer_with_score(2, llb_leads_implementation))
            },
            {
                'question_id': questions_id[id_questions[23]],
                'answer': int(map_answer_with_score(2, llb_performance_management))
            },
            {
                'question_id': questions_id[id_questions[24]],
                'answer': int(map_answer_with_score(2, llb_talents_utilised))
            },
            {
                'question_id': questions_id[id_questions[25]],
                'answer': int(map_answer_with_score(2, llb_conf_lv5_ldr))
            },
            {
                'question_id': questions_id[id_questions[26]],
                'answer': int(map_answer_with_score(2, llb_recognised_rewarded))
            },
            {
                'question_id': questions_id[id_questions[27]],
                'answer': int(map_answer_with_score(3, enb_ldr_support_system))
            },
            {
                'question_id': questions_id[id_questions[28]],
                'answer': int(map_answer_with_score(3, enb_ldr_time_resources))
            },
            {
                'question_id': questions_id[id_questions[29]],
                'answer': int(map_answer_with_score(1, enb_conf_lv2_ldr))
            },
            {
                'question_id': questions_id[id_questions[20]],
                'answer': int(map_answer_with_score(4, sfb_current_change_mgmt))
            },
            {
                'question_id': questions_id[id_questions[31]],
                'answer': int(map_answer_with_score(3, rsb_quick_remedial))
            },
            {
                'question_id': questions_id[id_questions[32]],
                'answer': int(map_answer_with_score(5, eeb_fear))
            },
            {
                'question_id': questions_id[id_questions[33]],
                'answer': int(map_answer_with_score(5, eeb_distress))
            },
            {
                'question_id': questions_id[id_questions[34]],
                'answer': int(map_answer_with_score(5, eeb_anger))
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

    driver = "Accountability"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Accountability")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Accountability")

    driver = "Team Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Team_Leadership")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title="Team Leadership", data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Team_Leadership")

    driver = "Business Leadership"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Business_Leadership")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Business_Leadership")

    driver = "Fear & Frustration"
    with st.expander(driver):
        fig = figure_scale_by_value(title=driver, data={driver: dict(drivers_average_score_data)[driver]})
        st.write("Click to view detailed metrics.")
        st.plotly_chart(fig, key="parent_Fear_and_Frustration")
        with st.expander(f"{driver} Drivers"):
            fig = figure_scale_by_value(title=driver, data=list_to_dict(drivers_question_data[driver]))
            st.write("Click to view detailed metrics.")
            st.plotly_chart(fig, key="child_Fear_and_Frustration")