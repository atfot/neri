import streamlit as st
from time import sleep
from streamlit_js_eval import streamlit_js_eval, get_geolocation
import json

if 'messages' not in st.session_state:
    st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )

    if 'screen_setting' not in st.session_state:
        x = streamlit_js_eval(js_expressions='window.innerWidth', key='WIDTH',  want_output = True)        
        if x is not None:   
            if x<662:
                st.session_state.screen_setting='mobile'
            if x>=662:
                st.session_state.screen_setting='pc'

    st.session_state.logged_in = False
    st.session_state.signin = False
    st.session_state.login_error = False

    if 'user_id' not in st.session_state:
        st.session_state.user_id = False
        st.session_state.password = False

    col1,col2=st.columns([6,4])
    with col1:
        language_selection=st.toggle('한국어/English')

    if not language_selection: 
        st.session_state['korean_mode']=1
        st.markdown('<p><b>한글 모드</b></p>', unsafe_allow_html=True)
        st.markdown('<center><h1>ᆞ네ᆞᆞ리ᆞ</h1></center>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right;"><p>로그인 해주세요</p></div>',unsafe_allow_html=True)
        
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        if st.session_state.screen_setting=='pc':
            col1, col2, col3 = st.columns([2,6,2])
            with col1:
                if st.button("새로 오신 분", type="secondary",use_container_width=True):
                    st.session_state.signin = True
            with col3:
                if st.button("로그인", type="primary",use_container_width=True):
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
        if st.session_state.screen_setting=='mobile':
            if st.button("로그인", type="primary",use_container_width=True):
                if username == st.session_state.user_id and password == st.session_state.password:
                    st.session_state.logged_in = True
                elif username == 'test' and password == 'test':
                    st.session_state.logged_in = True
                else:
                    st.session_state.login_error = True
            if st.button("새로 오신 분", type="secondary",use_container_width=True):
                    st.session_state.signin = True
            
        if st.session_state.get("logged_in", True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("성공적으로 로그인 되었습니다!")
                sleep(0.5)
                st.switch_page("pages/korean_chatbot_2.py")
        if st.session_state.get('login_error', True):
            col, col2, col3 = st.columns([2,6,2])
            with col2:
                st.error("아이디 또는 패스워드를 확인해주세요.")
        if st.session_state.get("login_error", False):
            pass
        if st.session_state.get('signin', True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("네리에 오신 것을 환영합니다!")
                sleep(0.5)
                st.switch_page("pages/signin.py")
        if st.session_state.get("signin", False):
            pass
    if language_selection: 
        st.session_state['korean_mode']=0
        st.markdown('<p><b>English mode</b></p>', unsafe_allow_html=True)
        st.markdown('<center><h1>ᆞNᆞᆞEᆞᆞRᆞᆞIᆞ</h1></center>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right;"><p>Please login</p></div>',unsafe_allow_html=True)

        username = st.text_input("ID")
        password = st.text_input("Password", type="password")

        if st.session_state.screen_setting=='pc':
            col1, col2, col3 = st.columns([2,6,2])
            with col1:
                if st.button("New User", type="secondary",use_container_width=True):
                    st.session_state.signin = True
            with col3:
                if st.button("Log in", type="primary",use_container_width=True):
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
        if st.session_state.screen_setting=='mobile':
            if st.button("Log in", type="primary",use_container_width=True):
                if username == st.session_state.user_id and password == st.session_state.password:
                    st.session_state.logged_in = True
                elif username == 'test' and password == 'test':
                    st.session_state.logged_in = True
                else:
                    st.session_state.login_error = True
            if st.button("New User", type="secondary",use_container_width=True):
                    st.session_state.signin = True

        if st.session_state.get("logged_in", True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/english_chatbot_2.py")
        if st.session_state.get("logged_in", False):
            pass
        if st.session_state.get('login_error', True):
            col, col2, col3 = st.columns([2.5,5,2.5])
            with col2:
                st.error("Incorrect ID or password")
        if st.session_state.get("login_error", False):
            pass
        if st.session_state.get('signin', True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("Welcome to Neri!")
                sleep(0.5)
                st.switch_page("pages/signin.py")
        if st.session_state.get("signin", False):
            pass


    

    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==0:
            #st.switch_page("pages/page2.py")
    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==1:
            #st.switch_page("pages/page4.py")


