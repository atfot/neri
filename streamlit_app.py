import streamlit as st
from time import sleep

try:
    if 'messages' not in st.session_state:
        st.set_page_config(
            page_title="Your AI Therapist, Neri",
            page_icon="🧊",
            layout="centered",
            menu_items=None
        )
        try:
            st.write(st.session_state.username)
        except:
            st.write('nothing went here')

        st.session_state.logged_in = False
        st.session_state.signin = False
        st.session_state.login_error = False

        col1,col2=st.columns([6,4])
        with col1:
            st.write('어떤 언어로 사용하실지 결정해주세요.')
            st.write("Please decide which language you'd like to use.")
            language_selection=st.toggle('한국어/English')
        st.title('')
        if language_selection: 
            st.session_state['korean_mode']=0
            col1,col2,col3=st.columns([4,2,4])
            with col2:
                st.title("Neri")
            st.title('')
            col1,col2=st.columns([5,5])
            with col2:
                st.write("""Please login 
                        
                        (username 'test', password 'test').""")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            col1, col2 = st.columns([8.6,1.4])
            with col1:
                if st.button("New User", type="secondary"):
                    st.session_state.signin = True
            with col2:
                if st.button("Log in", type="primary"):
                    if username == "test" and password == "test":
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
            if st.session_state.get("logged_in", True):
                col, col2, col3 = st.columns([3,4,3])
                with col2:
                    st.success("Logged in successfully!")
                    sleep(0.5)
                    st.switch_page("pages/page2.py")
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

        if not language_selection: 
            st.session_state['korean_mode']=1
            col1,col2,col3=st.columns([4,2,4])
            with col2:
                st.title("네리")
            st.title('')
            col1,col2=st.columns([4.7,5.3])
            with col2:
                st.write("""로그인해주세요 
                        
                        (유저이름 'test', 패스워드 'test').""")
            username = st.text_input("유저 이름")
            password = st.text_input("비밀번호", type="password")

            col1, col2 = st.columns([8.7,1.3])
            with col1:
                if st.button("새로 오신 분", type="secondary"):
                    st.session_state.signin = True
            with col2:
                if st.button("로그인", type="primary"):
                    if username == "test" and password == "test":
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
            if st.session_state.get("logged_in", True):
                col, col2, col3 = st.columns([3,4,3])
                with col2:
                    st.success("성공적으로 로그인 되었습니다!")
                    sleep(0.5)
                    st.switch_page("pages/page4.py")
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
except:
    if 'messages' in st.session_state:
        if st.session_state['korean_mode']==0:
            st.switch_page("pages/page2.py")
    if 'messages' in st.session_state:
        if st.session_state['korean_mode']==1:
            st.switch_page("pages/page4.py")


