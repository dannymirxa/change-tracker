# Initialize session state
import streamlit as st
from database_client import con

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