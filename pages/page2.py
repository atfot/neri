import streamlit as st
from korean_navigation import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()

if 'title' not in st.session_state:
    st.title('Hi')
if st.button('show the message'):
    
    st.write(st.session_state.conversations)
    st.write(st.session_state.message_summary)