import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="wide"
)
try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
st.write("개발자의 말 부분임. 나중에 적을 것임")