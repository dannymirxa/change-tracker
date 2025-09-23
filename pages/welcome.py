import streamlit as st
from datetime import datetime
# from database_client import con
from module.supabase_client import supabase

def show_welcome_page():
    st.session_state['surveys'] = "Employee Satisfaction Survey"
    st.session_state['cycle'] = "Cycle 2"
    response = (
        supabase.table("surveys")
        .select("created_time")
        .eq("name", f"{st.session_state['surveys']}")
        .eq("cycle", f"{st.session_state['cycle']}")
        .limit(1) 
        .execute() 
    )
    
    surveys_date = datetime.fromisoformat(response.data[0]['created_time']).date()
    st.session_state['surveys_date'] = surveys_date
    st.title(f"Welcome {st.session_state.get('username', 'User')} to {st.session_state['surveys']} {st.session_state['cycle']}")
    # Add further logic or components specific to the welcome page here

    if st.button("Go to Questionnaire", key="go_to_questionnaire"):
        st.session_state['page'] = 'questions'