import streamlit as st
from time import sleep
from streamlit_js_eval import streamlit_js_eval

if 'messages' not in st.session_state:
    if 'screen_setting' not in st.session_state:
        st.session_state.screen_setting = 'pc'  # default value

    st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered",
    menu_items=None
)

    if (x := streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH', want_output=True)) is not None:
        st.session_state.screen_setting = 'mobile' if x < 662 else 'pc'
    
    if 'korean_mode' not in st.session_state:
        st.session_state.korean_mode = 1

    col1,col2=st.columns([6,4])
    with col1:
        language_selection=st.toggle('**한국어/English**')
    st.session_state.korean_mode=0 if language_selection else 1

    if st.session_state['korean_mode']==1: 
        st.markdown('<p><h5>Korean Language Mode</h5></p>', unsafe_allow_html=True)

    if st.session_state['korean_mode']==0: 
        st.markdown('<p><h5>영어 모드</h5></p>', unsafe_allow_html=True)

    

    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==0:
            #st.switch_page("pages/page2.py")
    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==1:
            #st.switch_page("pages/page4.py")


