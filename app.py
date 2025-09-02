from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure
import streamlit as st
from pages import (
    show_login_page,
    show_welcome_page,
    show_questions,
    show_results_page
)

st.set_page_config(page_title="Change Tracker Dashboard", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 400px;
        margin-left: -400px;
    }
     
    """,
    unsafe_allow_html=True,
)

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