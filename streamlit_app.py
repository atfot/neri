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
    
    st.session_state.logged_in = False
    st.session_state.signin = False
    st.session_state.login_error = False

    if 'many_login_attempt' not in  st.session_state:
        st.session_state.many_login_attempt=False
        st.session_state.login_attempt=0

    if 'user_id' not in st.session_state:
        st.session_state.user_id = False
        st.session_state.password = False

    col1,col2=st.columns([6,4])
    with col1:
        language_selection=st.toggle('한국어/English')

    if not language_selection: 
        st.session_state['korean_mode']=1
        st.markdown('<p><b>Korean Language Mode</b></p>', unsafe_allow_html=True)
        st.markdown('<center><h1>ᆞ네ᆞᆞ리ᆞ</h1></center>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right;"><p>로그인 해주세요</p></div>',unsafe_allow_html=True)
        
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")

        if st.session_state.screen_setting=='pc':
            if st.button("로그인", type="primary",use_container_width=True):
                st.session_state.login_attempt+=1
                if st.session_state.login_attempt<6:
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
                if st.session_state.login_attempt>=6:
                    if st.session_state.login_error==True:
                        st.session_state.many_login_attempt = True

            col1, col2, col3 = st.columns([3.3,3.3,3.4])
            with col1:
                if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                    st.write('아직 제작중인 기능')
            with col2:
                if st.button("아이디 찾기", type="secondary",use_container_width=True):
                    st.write('아직 제작중인 기능')
            with col3:
                if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                    st.session_state.signin = True
        else:
            if st.button("로그인", type="primary",use_container_width=True):
                st.session_state.login_attempt+=1
                if st.session_state.login_attempt<6:
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
                if st.session_state.login_attempt>=6:
                    st.session_state.many_login_attempt = True
            if st.button("**새로 오신 분**", type="secondary",use_container_width=True):
                    st.session_state.signin = True
            if st.button("아이디 찾기", type="secondary",use_container_width=True):
                st.write('아직 제작중인 기능')
            if st.button("비밀번호 찾기", type="secondary",use_container_width=True):
                st.write('아직 제작중인 기능')
        
        if st.session_state.get("logged_in", True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("성공적으로 로그인 되었습니다!",  icon="✅")
                sleep(0.5)
                st.switch_page("pages/korean_chatbot_2.py")
        if st.session_state.get('login_error', True):
            col, col2, col3 = st.columns([2,6,2])
            with col2:
                st.error(f"아이디 또는 비밀번호를 확인해주세요({st.session_state.login_attempt}/5)")
        if st.session_state.get("login_error", False):
            pass
        if st.session_state.get('signin', True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("네리에 오신 것을 환영합니다!")
                sleep(0.5)
                st.switch_page("pages/signin.py")
        if st.session_state.get('many_login_attempt',True):
            col, col2, col3 = st.columns([2,6,2])
            with col2:
                st.error("""
                           아이디 또는 패스워드를 5번 이상 틀리셨습니다.
                           
                           아이디 또는 비밀번호 찾기를 통해 정보를 수정해주세요.""")
                st.stop()
        if st.session_state.get("signin", False):
            pass
    if language_selection: 
        st.session_state['korean_mode']=0
        st.markdown('<p><b>영어 모드</b></p>', unsafe_allow_html=True)
        st.markdown('<center><h1>ᆞNᆞᆞEᆞᆞRᆞᆞIᆞ</h1></center>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: right;"><p>Please login</p></div>',unsafe_allow_html=True)

        username = st.text_input("ID")
        password = st.text_input("Password", type="password")

        if st.session_state.screen_setting=='pc':
            if st.button("Log in", type="primary",use_container_width=True):
                st.session_state.login_attempt+=1
                if st.session_state.login_attempt<6:
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
                if st.session_state.login_attempt>=6:
                    if st.session_state.login_error==True:
                        st.session_state.many_login_attempt = True

            col1, col2, col3 = st.columns([3.3,3.3,3.4])
            with col1:
                if st.button("Find my ID", type="secondary",use_container_width=True):
                    st.write("I'm currently making this function")
            with col2:
                if st.button("Find my PW", type="secondary",use_container_width=True):
                    st.write("I'm currently making this function")
            with col3:
                if st.button("**New User**", type="secondary",use_container_width=True):
                    st.session_state.signin = True
        else:
            if st.button("Log in", type="primary",use_container_width=True):
                st.session_state.login_attempt+=1
                if st.session_state.login_attempt<6:
                    if username == st.session_state.user_id and password == st.session_state.password:
                        st.session_state.logged_in = True
                    elif username == 'test' and password == 'test':
                        st.session_state.logged_in = True
                    else:
                        st.session_state.login_error = True
                if st.session_state.login_attempt>=6:
                    if st.session_state.login_error==True:
                        st.session_state.many_login_attempt = True
            if st.button("**New User**", type="secondary",use_container_width=True):
                    st.session_state.signin = True
            if st.button("Find my ID", type="secondary",use_container_width=True):
                st.write("I'm currently making this function")
            if st.button("Find my PW", type="secondary",use_container_width=True):
                st.write("I'm currently making this function")

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
                st.error(f"Incorrect ID or password ({st.session_state.login_attempt}/5)")
        if st.session_state.get("login_error", False):
            pass
        if st.session_state.get('signin', True):
            col, col2, col3 = st.columns([3,4,3])
            with col2:
                st.success("Welcome to Neri!")
                sleep(0.5)
                st.switch_page("pages/signin.py")
        if st.session_state.get('many_login_attempt',True):
            col, col2, col3 = st.columns([2,6,2])
            with col2:
                st.error("""
                           You've entered your ID or password incorrectly more than 5 times.
                           
                           Please use 'Find my ID' or 'Find my PW' to correct your information.""")
                st.stop()
        if st.session_state.get("signin", False):
            pass


    

    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==0:
            #st.switch_page("pages/page2.py")
    #if 'messages' in st.session_state:
        #if st.session_state['korean_mode']==1:
            #st.switch_page("pages/page4.py")


