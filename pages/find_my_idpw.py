import streamlit as st
import time

st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="wide",
        menu_items=None
    )

if 'korean_mode' not in st.session_state:
    st.switch_page('streamlit_app.py')

if st.session_state.korean_mode==1:
    button=st.button("메인 화면으로")
    if button:
        del st.session_state.signin
        if 'many_login_attempt' in st.session_state:
            st.session_state.many_login_attempt
        st.switch_page("streamlit_app.py")
    col1,col2=st.columns([5,5])
    with col1:
        st.markdown('<center><h3>아이디 수정</h3></center>', unsafe_allow_html=True)
    with col2:
        st.markdown('<center><h3>패스워드 수정</h3></center>', unsafe_allow_html=True)
if st.session_state.korean_mode==0:
    button=st.button("Go to main", "https://neriuut.streamlit.app/")
    if button:
        del st.session_state.signin
        if 'many_login_attempt' in st.session_state:
            st.session_state.many_login_attempt
        st.switch_page("streamlit_app.py")
    col1,col2=st.columns([5,5])
    with col1:
        st.markdown('<center><h3>Fix your ID</h3></center>', unsafe_allow_html=True)
    with col2:
        st.markdown('<center><h3>Fix your PW</h3></center>', unsafe_allow_html=True)