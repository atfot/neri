import streamlit as st
from korean_menu import make_sidebar

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)
make_sidebar()

st.title('Welcome to Neri!')
st.title('')
st.write("""
Neri is an **AI Therapist Chatbot**, using **OpenAI's ChatGPT API**.
         
You can choose either GPT 3.5 or GPT 4.0 depending on your own needs.


         

""")