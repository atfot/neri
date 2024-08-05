import streamlit as st
from korean_menu import make_sidebar
from streamlit import session_state as sss

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="centered"
)

try:
    del sss.fix_info, sss.auth_email
except:
    pass
make_sidebar()
st.write("이걸 왜 만들었는지 적을 것")
st.write("어떻게 사용해야 하는지 적을 것")