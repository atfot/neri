import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss
from security import check

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
check()
st.write("개발자의 말 부분임. 나중에 적을 것임")