from navigation import make_sidebar
import streamlit as st

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

make_sidebar()

st.write(
    """
# Your problem solving rate

This part is also not finished.

Actually I was trying my best to perfect my AI chatbot.

"""
)
