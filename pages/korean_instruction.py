import streamlit as st
from korean_menu import make_sidebar

st.set_page_config(
    page_title="당신의 AI 심리상담사, 네리",
    page_icon="🧊",
    layout="wide"
)
make_sidebar()

if st.button('try'):
    st.write('success')