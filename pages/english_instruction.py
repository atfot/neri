import streamlit as st
from english_menu import make_sidebar

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
         
Jojo : Honestly I'm going to have to think hard about what to say shibal..


         

""")