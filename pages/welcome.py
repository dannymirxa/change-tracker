import streamlit as st
from database_client import con

def show_welcome_page():
    st.session_state['surveys'] = "Employee Satisfaction Survey"
    st.session_state['cycle'] = "Cycle 2"
    surveys_date = con.sql(f"SELECT DATE(created_time) FROM surveys \
                           WHERE name = '{st.session_state['surveys']}' AND cycle = '{st.session_state['cycle']}'\
                           LIMIT 1" \
                            ).fetchall()[0][0]
    st.session_state['surveys_date'] = surveys_date
    st.title(f"Welcome {st.session_state.get('username', 'User')} to {st.session_state['surveys']} {st.session_state['cycle']}")
    # Add further logic or components specific to the welcome page here

    if st.button("Go to Questionnaire", key="go_to_questionnaire"):
        st.session_state['page'] = 'questions'