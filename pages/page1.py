from navigation import make_sidebar
import streamlit as st

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

make_sidebar()

st.write('hi')
st.write(st.session_state.messages)
st.write(st.session_state.message_summary)
