from database_client import con
from modules import dict_to_nested_dict, list_to_dict, figure_scale_by_value
import streamlit as st
# from pages_survey import (
#     show_login_page,
#     show_welcome_page,
#     show_questions,
#     show_results_page
# )

from pages.login import show_login_page
from pages.welcome import show_welcome_page
from pages.questions import show_questions
from pages.result_latest import show_results_latest_page

st.set_page_config(page_title="Change Tracker Dashboard", layout="wide")
# st.markdown(
#     """
#     <style>
#     /* fixed-width sidebar when expanded */
#     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
#         width: 400px;
#         box-sizing: border-box;
#         padding-left: 12px; /* add left padding so inner highlight doesn't sit flush */
#         padding-right: 12px;
#     }
#     /* hide the sidebar visually when collapsed (keeps layout consistent) */
#     [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
#         width: 400px;
#         margin-left: -400px;
#         box-sizing: border-box;
#         padding-left: 12px;
#         padding-right: 12px;
#     }
#     /* confine any hover/selection highlights inside the sidebar
#        and add a smooth transition for open/close */
#     [data-testid="stSidebar"] {
#         transition: margin 0.25s ease, width 0.25s ease;
#         overflow: hidden; /* prevent inner elements from protruding outside */
#         position: relative;
#         z-index: 100; /* keep sidebar above page content */
#     }
#     /* ensure list items / selection boxes inside the sidebar do not overflow */
#     [data-testid="stSidebar"] .css-1d391kg, /* generic container class: safe guard */
#     [data-testid="stSidebar"] .stSidebar .block-container,
#     [data-testid="stSidebar"] .block-container {
#         overflow: hidden;
#         max-width: 100%;
#         box-sizing: border-box;
#     }
#     /* selection/highlight pill inside the sidebar: keep it inset from the edges */
#     [data-testid="stSidebar"] .css-1v0mbdj, /* selection pill class (Streamlit internal; best-effort) */
#     [data-testid="stSidebar"] .st-bsu,
#     [data-testid="stSidebar"] .st-cf {
#         display: inline-block;
#         margin-left: 8px;    /* space from left edge */
#         margin-right: 8px;   /* space from right edge */
#         width: calc(100% - 24px); /* fixed visual width relative to sidebar */
#         max-width: 360px;    /* cap width so it never fills entire sidebar */
#         overflow: hidden;
#         text-overflow: ellipsis;
#         white-space: nowrap;
#         border-radius: 8px;
#         box-sizing: border-box;
#         padding: 8px 12px;   /* comfortable inner padding */
#     }
#     /* small visual tweak so hovered/active pills look consistent */
#     [data-testid="stSidebar"] .css-1v0mbdj:hover,
#     [data-testid="stSidebar"] .st-bsu:hover,
#     [data-testid="stSidebar"] .st-cf:hover {
#         box-shadow: none;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# Ensure the session state is initialized
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

def navigate_pages():
    if st.session_state['page'] == 'login':
        show_login_page()
    elif st.session_state['page'] == 'welcome':
        show_welcome_page()
    elif st.session_state['page'] == 'questions':
        show_questions()
    elif st.session_state['page'] == 'results_latest':
        show_results_latest_page()

navigate_pages()
