from navigation import make_sidebar
import streamlit as st

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
    st.write(st.session_state.messages)
    st.write(st.session_state.message_summary)