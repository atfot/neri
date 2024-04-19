import streamlit as st
from time import sleep

if 'messages' not in st.session_state:
    st.set_page_config(
        page_title="Your AI Therapist, Neri",
        page_icon="🧊",
        layout="centered",
        menu_items=None
    )
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
        st.write('한글 모드')
        col1,col2,col3=st.columns([2,7,2])
        with col2:
            st.markdown("# ᆞNᆞᆞEᆞᆞRᆞᆞIᆞ")
        
        col1,col2=st.columns([22,5])
        with col2:
            st.write("로그인 해주세요")
        
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        col1, col2 = st.columns([9.8,1.3])
        with col1:
            if st.button("새로 오신 분", type="secondary"):
                st.session_state.signin = True
        with col2:
            if st.button("로그인", type="primary"):
                if username == st.session_state.user_id and password == st.session_state.password:
                    st.session_state.logged_in = True
                elif username == 'test' and password == 'test':
                    st.session_state.logged_in = True
                else:
                    st.session_state.login_error = True
        if st.session_state.get("logged_in", True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("성공적으로 로그인 되었습니다!")
                sleep(0.5)
                st.switch_page("pages/korean_chatbot_2.py")
        if st.session_state.get('login_error', True):
            col, col2, col3 = st.columns([2,6,2])
            with col2:
                st.error("유저 이름 또는 패스워드가 맞지 않습니다.")
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
        st.write('English mode')        
        col1,col2,col3=st.columns([2,7,2])
        with col2:
            st.markdown("# ᆞNᆞᆞEᆞᆞRᆞᆞIᆞ")
        
        col1,col2=st.columns([34.8,5])
        with col2:
            st.write("Please login")
        username = st.text_input("ID")
        password = st.text_input("Password", type="password")

        col1, col2 = st.columns([11.8,1.4])
        with col1:
            if st.button("New User", type="secondary"):
                st.session_state.signin = True
        with col2:
            if st.button("Log in", type="primary"):
                if username == st.session_state.user_id and password == st.session_state.password:
                    st.session_state.logged_in = True
                elif username == 'test' and password == 'test':
                    st.session_state.logged_in = True
                else:
                    st.session_state.login_error = True
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
                st.error("Incorrect username or password")
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


