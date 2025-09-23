import streamlit as st
import pandas as pd
import json
from database_client import con
from module.supabase_client import supabase

with open("map_answers_to_scores.json", "r") as json_file:
    answers_to_scores_map = json.load(json_file)

def map_answer_with_score(map_id: int, answer: str):
    return str(answers_to_scores_map[str(map_id)][answer])

# id_questions= dict(con.sql("SELECT id, questions FROM questions;").fetchall())
id_questions = supabase.table("questions").select("id, questions").execute().data
# questions_id= dict(con.sql("SELECT questions, id FROM questions;").fetchall())
questions_id = supabase.table("questions").select("questions, id").execute().data

def show_questions():
    st.title("Questions")

    """
    Accountability
    """
    st.header("Accountability", divider=True)

    llb_role_clarity = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 19),
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_role_clarity)}")
    llb_role_clarity_comment = st.text_area("Comments for the questions above:", height=30, key="llb_role_clarity_comment")

    llb_accountable = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 20),
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_accountable)}")
    llb_accountable_comment = st.text_area("Comments for the questions above:", height=30, key="llb_accountable_comment")
    
    llb_objectives_outcomes = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 21),
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, llb_objectives_outcomes)}")
    llb_objectives_outcomes_comment = st.text_area("Comments for the questions above:", height=30, key="llb_objectives_outcomes_comment")

    """
    Team Leadership
    """
    st.header("Team Leadership", divider=True)

    llb_leads_implementation = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 22),
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_leads_implementation)}")
    llb_leads_implementation_comment = st.text_area("Comments for the questions above:", height=30, key="llb_leads_implementation_comment")

    llb_performance_management = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 23),
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_performance_management)}")
    llb_performance_management_comment = st.text_area("Comments for the questions above:", height=30, key="llb_performance_management_comment")

    llb_talents_utilised = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 24),
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_talents_utilised)}")
    llb_talents_utilised_comment = st.text_area("Comments for the questions above:", height=30, key="llb_talents_utilised_comment")

    llb_conf_lv5_ldr = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 25),
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_conf_lv5_ldr)}")
    llb_conf_lv5_ldr_comment = st.text_area("Comments for the questions above:", height=30, key="llb_conf_lv5_ldr_comment")

    llb_recognised_rewarded = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 26),
        tuple(answers_to_scores_map['2'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(2, llb_recognised_rewarded)}")
    llb_recognised_rewarded_comment = st.text_area("Comments for the questions above:", height=30, key="llb_recognised_rewarded_comment")

    """
    Business Leadership
    """
    st.header("Business Leadership", divider=True)

    enb_ldr_support_system = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 27),
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, enb_ldr_support_system)}")
    enb_ldr_support_system_comment = st.text_area("Comments for the questions above:", height=30, key="enb_ldr_support_system_comment")

    enb_ldr_time_resources = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 28),
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, enb_ldr_time_resources)}")
    enb_ldr_time_resources_comment = st.text_area("Comments for the questions above:", height=30, key="enb_ldr_time_resources_comment")

    enb_conf_lv2_ldr = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 29),
        tuple(answers_to_scores_map['1'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(1, enb_conf_lv2_ldr)}")
    enb_conf_lv2_ldr_comment = st.text_area("Comments for the questions above:", height=30, key="enb_conf_lv2_ldr_comment")

    sfb_current_change_mgmt = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 30),
        tuple(answers_to_scores_map['4'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(4, sfb_current_change_mgmt)}")
    sfb_current_change_mgmt_comment = st.text_area("Comments for the questions above:", height=30, key="sfb_current_change_mgmt_comment")

    rsb_quick_remedial = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 31),
        tuple(answers_to_scores_map['3'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(3, rsb_quick_remedial)}")
    rsb_quick_remedial_comment = st.text_area("Comments for the questions above:", height=30, key="rsb_quick_remedial_comment")

    """
    Fear and Frustration
    """
    st.header("Fear and Frustration", divider=True)

    eeb_fear = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 32),
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_fear)}")
    eeb_fear_comment = st.text_area("Comments for the questions above:", height=30, key="eeb_fear_comment")

    eeb_distress = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 33),
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_distress)}")
    eeb_distress_comment = st.text_area("Comments for the questions above:", height=30, key="eeb_distress_comment")

    eeb_anger = st.radio(
        next(item['questions'] for item in id_questions if item["id"] == 34),
        tuple(answers_to_scores_map['5'].keys()),
        horizontal=True
    )
    st.write(f"Your gave score: {map_answer_with_score(5, eeb_anger)}")
    eeb_anger_comment = st.text_area("Comments for the questions above:", height=30, key="eeb_anger_comment")

    # Collect user answers into a dictionary
    answers = {
        'user_id': con.sql(f"SELECT id FROM users where username = '{st.session_state.get('username')}'").fetchall()[0][0] ,  # Assuming username can serve as user_id here
        'responses': [
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 19),
                'answer': int(map_answer_with_score(1, llb_role_clarity)),
                'comment': llb_role_clarity_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 20),
                'answer': int(map_answer_with_score(1, llb_accountable)),
                'comment': llb_accountable_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 21),
                'answer': int(map_answer_with_score(1,  llb_objectives_outcomes)),
                'comment': llb_objectives_outcomes_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 22),
                'answer': int(map_answer_with_score(2, llb_leads_implementation)),
                'comment': llb_leads_implementation_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 23),
                'answer': int(map_answer_with_score(2, llb_performance_management)),
                'comment': llb_performance_management_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 24),
                'answer': int(map_answer_with_score(2, llb_talents_utilised)),
                'comment': llb_talents_utilised_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 25),
                'answer': int(map_answer_with_score(2, llb_conf_lv5_ldr)),
                'comment': llb_conf_lv5_ldr_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 26),
                'answer': int(map_answer_with_score(2, llb_recognised_rewarded)),
                'comment': llb_recognised_rewarded_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 27),
                'answer': int(map_answer_with_score(3, enb_ldr_support_system)),
                'comment': enb_ldr_support_system_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 28),
                'answer': int(map_answer_with_score(3, enb_ldr_time_resources)),
                'comment': enb_ldr_time_resources_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 29),
                'answer': int(map_answer_with_score(1, enb_conf_lv2_ldr)),
                'comment': enb_conf_lv2_ldr_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 20),
                'answer': int(map_answer_with_score(4, sfb_current_change_mgmt)),
                'comment': sfb_current_change_mgmt_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 31),
                'answer': int(map_answer_with_score(3, rsb_quick_remedial)),
                'comment': rsb_quick_remedial_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 32),
                'answer': int(map_answer_with_score(5, eeb_fear)),
                'comment': eeb_fear_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 33),
                'answer': int(map_answer_with_score(5, eeb_distress)),
                'comment': eeb_distress_comment
            },
            {
                'question_id': next(item['id'] for item in id_questions if item["id"] == 34),
                'answer': int(map_answer_with_score(5, eeb_anger)),
                'comment': eeb_anger_comment
            }
        ]
    }

    # Show Button to Save Answers
    if st.button("Submit Answers", key="submit_answers"):
        # Convert JSON to pandas DataFrame and display
        responses_df = pd.json_normalize(answers, record_path='responses', meta='user_id')
        st.write("Answers DataFrame ready for insertion:")
        st.dataframe(responses_df)
        # Insert data from DataFrame into the DuckDB answers table
        for index, row in responses_df.iterrows():
            # Sanitize and coerce types to avoid DuckDB parameter errors (e.g. NaN or numpy types)
            user_id = int(row['user_id'])
            question_id = int(row['question_id'])
            answer_val = int(row['answer']) if pd.notna(row['answer']) else None
            comment_val = row['comment'] if (pd.notna(row.get('comment')) and row.get('comment') is not None) else ""
            con.execute(
                "INSERT INTO answers (user_id, questions_id, answers, comments) VALUES (?, ?, ?, ?)",
                (user_id, question_id, answer_val, comment_val)
            )
        st.success("Responses successfully inserted into the database.")
        # Navigate to results page only after inserts are complete, then rerun so the results page reads fresh data
        st.session_state['page'] = 'results_latest'
        st.rerun()
