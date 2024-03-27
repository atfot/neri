import streamlit as st
from time import sleep

st.set_page_config(
    page_title="Your AI Therapist, Neri",
    page_icon="🧊",
    layout="centered",
    menu_items=None
)

col1,col2=st.columns([4,6])
with col1:
    language_selection=st.toggle('한국어/English')
st.title('')
if language_selection: 
    st.session_state['korean_mode']=0
    if 'login_error' in st.session_state:
        del st.session_state.login_error
    else:
        pass
    col1,col2,col3=st.columns([4,2,4])
    with col2:
        st.title("Neri")
    st.title('')
    col1,col2=st.columns([5,5])
    with col2:
        st.write("Please login (username `test`, password `test`).")
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
                
    if 'logged_in' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page4.py")
    if 'logged_in' not in st.session_state:
        pass
    if 'login_error' in st.session_state:
        col, col2, col3 = st.columns([2.5,5,2.5])
        with col2:
            st.error("Incorrect username or password")
    if 'login_error' not in st.session_state:
        pass
    if 'signin' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("Welcome to Neri!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    if 'signin' not in st.session_state:
        pass

if not language_selection: 
    st.session_state['korean_mode']=1
    if 'login_error' in st.session_state:
        del st.session_state.login_error
    else:
        pass
    col1,col2,col3=st.columns([4,2,4])
    with col2:
        st.title("네리")
    st.title('')
    col1,col2=st.columns([4.7,5.3])
    with col2:
        st.write("로그인해주세요 (유저이름 `test`, 패스워드 `test`).")
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
    if 'logged_in' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("성공적으로 로그인 되었습니다!")
            sleep(0.5)
            st.switch_page("pages/page4.py")
    if 'login_error' in st.session_state:
        col, col2, col3 = st.columns([2,6,2])
        with col2:
            st.error("유저 이름 또는 패스워드가 맞지 않습니다.")
    if 'login_error' not in st.session_state:
        pass
    if 'logged_in' not in st.session_state:
        pass
    if 'signin' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("네리에 오신 것을 환영합니다!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    if 'signin' not in st.session_state:
        pass